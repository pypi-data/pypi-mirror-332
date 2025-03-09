from .base_tool import BaseTool
from typing import Dict, Any, Optional, List
from pydantic import Field
import threading
import logging
import time
import uuid
import json
import re

# Configure logging
logger = logging.getLogger(__name__)

class WebBrowserAsyncAdapter(BaseTool):
    """
    Async adapter for the WebBrowser tool that allows it to be used in an async context.
    This wrapper runs the WebBrowser tool in a separate thread and provides detailed progress updates.
    """
    name: str = Field("WebBrowserAsync", description="Async version of WebBrowser tool")
    description: str = Field(
        "Asynchronous web automation tool with multi-strategy element identification, self-healing selectors, and real-time progress reporting.",
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
            # Create a custom logger for the WebBrowser tool
            web_browser_logger = self._create_custom_logger()
            
            # Pass any parameters to the WebBrowser tool
            self._web_browser_tool = WebBrowserTool(*args, **kwargs)
            
            # Attach our custom logger to capture logs
            object.__setattr__(self._web_browser_tool, "logger", web_browser_logger)
        except ImportError:
            raise ImportError("WebBrowserTool not found. Make sure it's properly installed.")
        
        # Initialize the tasks dictionary
        object.__setattr__(self, "_tasks", {})
        
        # Set up logging
        object.__setattr__(self, "logger", logging.getLogger(__name__))
    
    def _create_custom_logger(self):
        """Create a custom logger that will capture logs for progress updates"""
        logger = logging.getLogger(f"webbrowser_async_{uuid.uuid4()}")
        logger.setLevel(logging.INFO)
        
        # Create a handler that will store logs in memory
        class TaskProgressHandler(logging.Handler):
            def __init__(self, task_id=None):
                super().__init__()
                self.logs = []
                self.task_id = task_id
                self.parent = None  # Reference to the adapter
                
            def emit(self, record):
                log_entry = {
                    "timestamp": time.time(),
                    "level": record.levelname,
                    "message": self.format(record)
                }
                
                self.logs.append(log_entry)
                
                # If parent and task_id are set, update the task's progress
                if self.parent and self.task_id and self.task_id in self.parent._tasks:
                    # Parse the message to determine task progress
                    task_info = self._parse_log_message(record.message)
                    if task_info:
                        self.parent._tasks[self.task_id]["steps"].append(task_info)
                        
                        # Update progress percentage based on completed tasks
                        if "Executing task:" in record.message:
                            # Extract the task number if it's in the format "Task X of Y"
                            match = re.search(r"task (\d+) of (\d+)", record.message.lower())
                            if match:
                                current = int(match.group(1))
                                total = int(match.group(2))
                                progress = min(int((current / total) * 100), 95)  # Cap at 95% until fully done
                                self.parent._tasks[self.task_id]["progress"] = progress
                            elif "plan contains" in record.message.lower():
                                # Extract the total number of tasks
                                match = re.search(r"plan contains (\d+) tasks", record.message.lower())
                                if match:
                                    self.parent._tasks[self.task_id]["total_tasks"] = int(match.group(1))
                                    self.parent._tasks[self.task_id]["current_task"] = 0
                            else:
                                # Increment the current task
                                current = self.parent._tasks[self.task_id].get("current_task", 0) + 1
                                total = self.parent._tasks[self.task_id].get("total_tasks", 0)
                                if total > 0:
                                    progress = min(int((current / total) * 100), 95)
                                    self.parent._tasks[self.task_id]["progress"] = progress
                                    self.parent._tasks[self.task_id]["current_task"] = current
                        
                        # Set final progress to 100% when complete
                        if "Total execution time:" in record.message:
                            self.parent._tasks[self.task_id]["progress"] = 100
            
            def _parse_log_message(self, message: str) -> Optional[Dict[str, Any]]:
                """Parse log messages to extract task info"""
                # Check for task execution
                if "Executing task:" in message:
                    task_description = message.replace("Executing task:", "").strip()
                    return {
                        "type": "task_start",
                        "description": task_description,
                        "status": "running"
                    }
                # Check for action completion
                elif "completed in" in message and "Action" in message:
                    match = re.search(r"Action '([^']+)' completed in ([0-9.]+) seconds", message)
                    if match:
                        action = match.group(1)
                        duration = float(match.group(2))
                        return {
                            "type": "task_complete",
                            "action": action,
                            "duration": duration,
                            "status": "success"
                        }
                # Check for errors
                elif "failed:" in message or "error:" in message.lower():
                    return {
                        "type": "error",
                        "message": message,
                        "status": "error"
                    }
                # Check for plan generation
                elif "Plan contains" in message:
                    match = re.search(r"Plan contains (\d+) tasks", message)
                    if match:
                        total_tasks = int(match.group(1))
                        return {
                            "type": "plan",
                            "total_tasks": total_tasks,
                            "status": "planning"
                        }
                # Default progress update
                elif any(keyword in message.lower() for keyword in ["waiting", "navigating", "typing", "clicking"]):
                    return {
                        "type": "progress",
                        "message": message,
                        "status": "running"
                    }
                return None
        
        # Create our handler instance
        handler = TaskProgressHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        # Store the handler for later use
        object.__setattr__(self, "_log_handler", handler)
        
        return logger
    
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
            "status": "initializing",
            "start_time": time.time(),
            "result": None,
            "error": None,
            "progress": 0,
            "steps": [],
            "current_task": 0,
            "total_tasks": 0
        }
        
        # Make sure the tool has access to the LLM
        if not self._web_browser_tool.llm and self.llm:
            self._web_browser_tool.llm = self.llm
        
        # Update the log handler with task ID and parent reference
        if hasattr(self, "_log_handler"):
            self._log_handler.task_id = task_id
            self._log_handler.parent = self
        
        # Start the tool execution in a background thread
        thread = threading.Thread(
            target=self._run_browser_in_thread,
            args=(task_id, input_data),
            daemon=True
        )
        thread.start()
        
        # Update status to running
        self._tasks[task_id]["status"] = "running"
        
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
            # Ensure we have a query parameter
            if "query" not in input_data and "message" in input_data:
                input_data["query"] = input_data["message"]
                del input_data["message"]
            
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
                "progress": 100,
                "end_time": time.time()
            })
    
    def get_task_status(self, task_id: str) -> Dict[str, Any]:
        """
        Get the status of a background task with detailed progress information.
        
        Args:
            task_id (str): The unique task ID
            
        Returns:
            Dict[str, Any]: The current status of the task with step-by-step progress
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
            "duration": round(duration, 2),
            "steps": task_info.get("steps", []),
            "current_task": task_info.get("current_task", 0),
            "total_tasks": task_info.get("total_tasks", 0)
        }
        
        # Add result or error if available
        if task_info["status"] == "completed":
            response["result"] = task_info["result"]
            
            # Clean up completed tasks after retrieval, but not too soon
            # Only clean up if it's been at least 5 minutes since completion
            if duration > 300:
                self._tasks.pop(task_id, None)
                
        elif task_info["status"] == "error":
            response["error"] = task_info["error"]
        
        return response