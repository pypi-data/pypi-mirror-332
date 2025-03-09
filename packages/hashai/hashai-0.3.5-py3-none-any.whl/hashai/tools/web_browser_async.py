from .base_tool import BaseTool
from typing import Dict, Any, Optional
from pydantic import Field
import threading
import logging
import time
import uuid

# Configure logging
logger = logging.getLogger(__name__)

class WebBrowserAsyncAdapter(BaseTool):
    """
    Async adapter for the WebBrowser tool that allows it to be used in an async context.
    This wrapper runs the WebBrowser tool in a separate thread and provides status updates.
    """
    name: str = Field("WebBrowserAsync", description="Async version of WebBrowser tool")
    description: str = Field(
        "Asynchronous web automation tool with multi-strategy element identification, self-healing selectors, and robust error recovery.",
        description="Tool description"
    )
    
    # Reference to the original synchronous WebBrowser tool
    _web_browser_tool: Optional[Any] = None
    
    # Track running tasks
    _tasks: Dict[str, Dict[str, Any]] = {}
    
    class Config:
        arbitrary_types_allowed = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically import the WebBrowser tool
        try:
            from .web_browser import WebBrowserTool
            self._web_browser_tool = WebBrowserTool(*args, **kwargs)
        except ImportError:
            raise ImportError("WebBrowserTool not found. Make sure it's properly installed.")
        
        # Initialize the tasks dictionary
        object.__setattr__(self, "_tasks", {})
        
        # Set up logging
        object.__setattr__(self, "logger", logging.getLogger(__name__))
    
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the WebBrowser tool asynchronously by running it in a background thread.
        
        Args:
            input_data (Dict[str, Any]): Input parameters for the WebBrowser tool
            
        Returns:
            Dict[str, Any]: A task ID that can be used to poll for results
        """
        if not self._web_browser_tool:
            return {
                "status": "error",
                "message": "WebBrowserTool not initialized"
            }
        
        # Generate a unique task ID
        task_id = str(uuid.uuid4())
        
        # Store task information
        self._tasks[task_id] = {
            "status": "running",
            "start_time": time.time(),
            "result": None,
            "error": None,
            "progress": 0
        }
        
        # Make sure the tool has access to the LLM
        if not self._web_browser_tool.llm and self.llm:
            self._web_browser_tool.llm = self.llm
        
        # Start the tool execution in a background thread
        thread = threading.Thread(
            target=self._run_browser_in_thread,
            args=(task_id, input_data),
            daemon=True
        )
        thread.start()
        
        return {
            "status": "running",
            "task_id": task_id,
            "message": "Browser automation started in background thread"
        }
    
    def _run_browser_in_thread(self, task_id: str, input_data: Dict[str, Any]) -> None:
        """
        Run the WebBrowser tool in a background thread.
        
        Args:
            task_id (str): The unique task ID
            input_data (Dict[str, Any]): Input parameters for the WebBrowser tool
        """
        try:
            # Execute the WebBrowser tool
            result = self._web_browser_tool.execute(input_data)
            
            # Update task status
            self._tasks[task_id].update({
                "status": "completed",
                "result": result,
                "progress": 100,
                "end_time": time.time()
            })
        except Exception as e:
            # Log the error
            self.logger.error(f"Error running WebBrowser tool: {e}")
            
            # Update task status
            self._tasks[task_id].update({
                "status": "error",
                "error": str(e),
                "end_time": time.time()
            })
    
    def get_task_status(self, task_id: str) -> Dict[str, Any]:
        """
        Get the status of a background task.
        
        Args:
            task_id (str): The unique task ID
            
        Returns:
            Dict[str, Any]: The current status of the task
        """
        if task_id not in self._tasks:
            return {
                "status": "error",
                "message": f"Task {task_id} not found"
            }
        
        task_info = self._tasks[task_id]
        
        # Calculate task duration
        duration = (task_info.get("end_time") or time.time()) - task_info["start_time"]
        
        # Create response with task information
        response = {
            "status": task_info["status"],
            "progress": task_info["progress"],
            "duration": duration
        }
        
        # Add result or error if available
        if task_info["status"] == "completed":
            response["result"] = task_info["result"]
            
            # Clean up completed tasks after retrieval
            # Only clean up if it's been at least 5 minutes since completion
            if duration > 300:
                self._tasks.pop(task_id, None)
                
        elif task_info["status"] == "error":
            response["error"] = task_info["error"]
        
        return response