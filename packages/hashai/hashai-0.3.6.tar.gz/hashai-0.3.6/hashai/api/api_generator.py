from fastapi import FastAPI, HTTPException, Request, BackgroundTasks, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any, Union
import threading
import logging
import uuid

# Configure logging
logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    message: str = Field(..., description="User message to process")
    tool_params: Optional[Dict[str, Any]] = Field(None, description="Additional parameters for tool execution")
    stream: Optional[bool] = Field(False, description="Whether to stream the response")

class ToolRequest(BaseModel):
    tool_name: str = Field(..., description="Name of the tool to execute")
    input_data: Dict[str, Any] = Field(..., description="Input data for the tool")
    
class APIGenerator:
    def __init__(self, assistant):
        """
        Initialize the APIGenerator with the given assistant.

        Args:
            assistant: The assistant instance for which the API is being created.
        """
        self.assistant = assistant
        self.app = self._create_fastapi_app()
        self._background_tasks = {}
        
    def _create_fastapi_app(self) -> FastAPI:
        """
        Create a FastAPI app with enhanced endpoints for the assistant and its tools.
        """
        app = FastAPI(title=f"{self.assistant.name or 'Assistant'} API", 
                    description=self.assistant.description or "API for interacting with the assistant")

        # Default CORS settings (allow all)
        cors_config = {
            "allow_origins": ["*"],
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }

        # Override default CORS settings with user-provided settings
        if self.assistant.api_config and "cors" in self.assistant.api_config:
            cors_config.update(self.assistant.api_config["cors"])

        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_config["allow_origins"],
            allow_credentials=cors_config["allow_credentials"],
            allow_methods=cors_config["allow_methods"],
            allow_headers=cors_config["allow_headers"],
        )

        @app.post("/chat")
        async def chat(
            request: Optional[ChatRequest] = None, 
            message: Optional[str] = None
        ):
            """
            Endpoint to interact with the assistant.
            
            Supports both:
            - Query parameter: /chat?message=your_message
            - JSON body: {"message": "your_message"}
            """
            try:
                # Get message from either body or query param
                actual_message = None
                stream = False
                tool_params = None
                
                if request:
                    actual_message = request.message
                    stream = request.stream
                    tool_params = request.tool_params
                elif message:
                    actual_message = message
                
                if not actual_message:
                    raise HTTPException(status_code=400, detail="Message is required")
                    
                if stream:
                    task_id = self._start_streaming_task(actual_message, tool_params)
                    return {"task_id": task_id, "status": "streaming"}
                else:
                    response = self.assistant.print_response(message=actual_message)
                    if self.assistant.json_output:
                        return response
                    else:
                        return {"response": response}
            except Exception as e:
                logger.error(f"Error in chat endpoint: {e}")
                raise HTTPException(status_code=500, detail=str(e))

        @app.get("/stream/{task_id}")
        async def get_stream_status(task_id: str):
            """
            Get the status of a streaming task.
            """
            if task_id not in self._background_tasks:
                raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found")
            
            task_info = self._background_tasks[task_id]
            if task_info["status"] == "completed":
                # Clean up completed task
                result = task_info["result"]
                del self._background_tasks[task_id]
                return {"status": "completed", "response": result}
            elif task_info["status"] == "error":
                error = task_info["error"]
                del self._background_tasks[task_id]
                return {"status": "error", "error": str(error)}
            else:
                return {"status": "processing"}

        @app.get("/tools")
        async def get_tools():
            """
            Endpoint to get the list of tools available to the assistant.
            """
            if not self.assistant.tools:
                return {"tools": []}
                
            tools_info = []
            for tool in self.assistant.tools:
                tool_info = {
                    "name": tool.name,
                    "description": tool.description
                }
                # Add additional tool fields that might be useful
                for field_name, field in tool.__fields__.items():
                    if field_name not in ["name", "description", "llm"] and hasattr(tool, field_name):
                        value = getattr(tool, field_name)
                        if not callable(value):
                            tool_info[field_name] = value
                tools_info.append(tool_info)
            
            return {"tools": tools_info}

        # Add endpoint to execute tools directly
        @app.post("/tools/{tool_name}")
        async def execute_tool(
            tool_name: str, 
            background_tasks: BackgroundTasks,
            input_data: Dict[str, Any] = Body(...),
            async_execution: bool = False
        ):
            """
            Execute a specific tool directly.
            """
            # Find the requested tool
            tool = next((t for t in self.assistant.tools if t.name.lower() == tool_name.lower()), None)
            if not tool:
                raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
            
            # Check if the tool needs to run asynchronously (like WebBrowser)
            if async_execution or tool.name == "WebBrowserAsync" or tool.name == "WebBrowser":
                task_id = f"tool_{tool_name}_{uuid.uuid4()}"
                self._background_tasks[task_id] = {"status": "processing"}
                
                background_tasks.add_task(
                    self._execute_tool_in_background,
                    task_id=task_id,
                    tool=tool,
                    input_data=input_data
                )
                
                return {"task_id": task_id, "status": "processing"}
            else:
                try:
                    # Set the LLM instance if not already set
                    if not tool.llm and self.assistant.llm_instance:
                        tool.llm = self.assistant.llm_instance
                    
                    # Execute the tool
                    result = tool.execute(input_data)
                    return {"status": "success", "result": result}
                except Exception as e:
                    logger.error(f"Error executing tool '{tool_name}': {e}")
                    raise HTTPException(status_code=500, detail=str(e))

        @app.get("/tools/status/{task_id}")
        async def get_tool_status(task_id: str):
            """
            Get the status of an asynchronous tool execution.
            """
            if task_id not in self._background_tasks:
                raise HTTPException(status_code=404, detail=f"Task ID {task_id} not found")
            
            task_info = self._background_tasks[task_id]
            if task_info["status"] == "completed":
                # Clean up completed task
                result = task_info["result"]
                del self._background_tasks[task_id]
                return {"status": "completed", "result": result}
            elif task_info["status"] == "error":
                error = task_info["error"]
                del self._background_tasks[task_id]
                return {"status": "error", "error": str(error)}
            else:
                return {"status": "processing"}
                
        # Add endpoint for health check
        @app.get("/health")
        async def health_check():
            """
            Simple health check endpoint.
            """
            return {"status": "ok", "assistant": self.assistant.name or "Assistant"}

        # Add metadata endpoint with assistant info
        @app.get("/info")
        async def agent_info():
            """
            Get information about the assistant.
            """
            info = {
                "name": self.assistant.name,
                "description": self.assistant.description,
                "llm_provider": self.assistant.llm,
                "llm_model": self.assistant.llm_model,
                "has_tools": len(self.assistant.tools or []) > 0,
                "has_memory": bool(self.assistant.memory),
                "has_rag": bool(self.assistant.rag and self.assistant.rag != "None")
            }
            return info

        # Add endpoint for memory management
        if hasattr(self.assistant, "memory") and self.assistant.memory:
            @app.post("/memory/clear")
            async def clear_memory():
                """
                Clear the assistant's conversation memory.
                """
                self.assistant.memory.clear()
                return {"status": "success", "message": "Memory cleared"}

            @app.get("/memory")
            async def get_memory():
                """
                Get the assistant's conversation memory.
                """
                if hasattr(self.assistant.memory, "storage") and self.assistant.memory.storage:
                    entries = self.assistant.memory.storage.retrieve()
                    memory_entries = [{"role": e.role, "content": e.content, "timestamp": e.timestamp} for e in entries]
                    return {"memory": memory_entries}
                return {"memory": []}

        # Implement image processing if the LLM supports it
        if hasattr(self.assistant.llm_instance, "supports_vision") and self.assistant.llm_instance.supports_vision:
            @app.post("/process_image")
            async def process_image(background_tasks: BackgroundTasks, request: Request):
                """
                Process an image with the assistant.
                """
                form = await request.form()
                
                # Get the prompt
                prompt = form.get("prompt", "")
                
                # Get the image file
                image_file = form.get("image")
                if not image_file:
                    raise HTTPException(status_code=400, detail="No image provided")
                
                try:
                    # Read image data
                    image_data = await image_file.read()
                    
                    # Check if streaming is requested
                    stream = form.get("stream", "").lower() == "true"
                    
                    if stream:
                        task_id = f"image_{uuid.uuid4()}"
                        self._background_tasks[task_id] = {"status": "processing"}
                        
                        background_tasks.add_task(
                            self._process_image_in_background,
                            task_id=task_id,
                            prompt=prompt,
                            image_data=image_data
                        )
                        
                        return {"task_id": task_id, "status": "processing"}
                    else:
                        # Process the image
                        from io import BytesIO
                        from PIL import Image
                        
                        # Convert bytes to PIL Image
                        image = Image.open(BytesIO(image_data))
                        
                        # Generate response
                        response = self.assistant._generate_response_from_image(prompt, image)
                        
                        return {"status": "success", "response": response}
                except Exception as e:
                    logger.error(f"Error processing image: {e}")
                    raise HTTPException(status_code=500, detail=str(e))

        return app

    def _start_streaming_task(self, message: str, tool_params: Optional[Dict[str, Any]] = None) -> str:
        """Start a background task for streaming responses"""
        task_id = f"stream_{uuid.uuid4()}"
        self._background_tasks[task_id] = {"status": "processing"}
        
        # Start the task in a separate thread
        threading.Thread(
            target=self._execute_agent_in_background,
            args=(task_id, message, tool_params),
            daemon=True
        ).start()
        
        return task_id
        
    def _execute_agent_in_background(self, task_id: str, message: str, tool_params: Optional[Dict[str, Any]] = None):
        """Execute the assistant in a background thread"""
        try:
            kwargs = {}
            if tool_params:
                kwargs.update(tool_params)
                
            response = self.assistant._generate_response(message=message, **kwargs)
            self._background_tasks[task_id] = {
                "status": "completed",
                "result": response
            }
        except Exception as e:
            logger.error(f"Error in background task: {e}")
            self._background_tasks[task_id] = {
                "status": "error",
                "error": str(e)
            }
            
    def _execute_tool_in_background(self, task_id: str, tool, input_data: Dict[str, Any]):
        """Execute a tool in a background thread"""
        try:
            # Set the LLM instance if not already set
            if not tool.llm and self.assistant.llm_instance:
                tool.llm = self.assistant.llm_instance
                
            # Execute the tool
            result = tool.execute(input_data)
            self._background_tasks[task_id] = {
                "status": "completed",
                "result": result
            }
        except Exception as e:
            logger.error(f"Error executing tool: {e}")
            self._background_tasks[task_id] = {
                "status": "error",
                "error": str(e)
            }
            
    def _process_image_in_background(self, task_id: str, prompt: str, image_data: bytes):
        """Process an image in a background thread"""
        try:
            from io import BytesIO
            from PIL import Image
            
            # Convert bytes to PIL Image
            image = Image.open(BytesIO(image_data))
            
            # Generate response
            response = self.assistant._generate_response_from_image(prompt, image)
            
            self._background_tasks[task_id] = {
                "status": "completed",
                "result": response
            }
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            self._background_tasks[task_id] = {
                "status": "error",
                "error": str(e)
            }

    def run(self, host: str = "0.0.0.0", port: int = 8000):
        """
        Run the FastAPI app.

        Args:
            host (str): The host address to run the API server on. Default is "0.0.0.0".
            port (int): The port to run the API server on. Default is 8000.
        """
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)