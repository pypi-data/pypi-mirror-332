import functools
import time
from typing import Callable, Any, Optional
import inspect
import requests
from requests.models import Response
import json
import httpx

class MockedResponse(Response):
    def __init__(self, status_code: int, content: Any, headers: dict):
        super().__init__()
        self.status_code = status_code
        self._content = json.dumps(content).encode('utf-8') if isinstance(content, (dict, list)) else str(content).encode('utf-8')
        self.headers = headers

class RequestCatcher:
    def __init__(self, explorer_url: str = "http://localhost:8000"):
        self.explorer_url = explorer_url.rstrip('/')
    
    def catch_requests(self, source_name: Optional[str] = None):
        """
        Decorator to catch and log HTTP requests to the request explorer service.
        
        Args:
            source_name: Optional name to identify the source of requests
        
        Example:
            catcher = RequestCatcher("http://localhost:8000")
            
            @catcher.catch_requests("my_service")
            def fetch_data():
                response = requests.get('https://api.example.com/data')
                return response.json()
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Store original request methods
                original_get = requests.get
                original_post = requests.post
                original_put = requests.put
                original_delete = requests.delete
                original_patch = requests.patch
                
                def create_interceptor(original_method: Callable, method_name: str) -> Callable:
                    def intercepted_request(*request_args, **request_kwargs) -> Response:
                        start_time = time.time()
                        
                        # Get the URL from args or kwargs
                        url = request_args[0] if request_args else request_kwargs.get('url')
                        
                        # Extract request details
                        headers = request_kwargs.get('headers', {})
                        params = request_kwargs.get('params', {})
                        body = request_kwargs.get('json') or request_kwargs.get('data')
                        
                        try:
                            # Check for mock first
                            with httpx.Client() as client:
                                explorer_response = client.post(
                                    f"{self.explorer_url}/api/check_mock",
                                    json={
                                        "url": url,
                                        "method": method_name,
                                    },
                                    timeout=2.0
                                )
                                explorer_data = explorer_response.json()
                            
                            if explorer_data.get("is_mocked"):
                                mock_data = explorer_data["mock"]
                                response = MockedResponse(
                                    status_code=mock_data["status"],
                                    content=mock_data["body"],
                                    headers=mock_data["headers"]
                                )
                            else:
                                # Make the actual request if no mock
                                response = original_method(*request_args, **request_kwargs)
                            
                            duration = (time.time() - start_time) * 1000  # Convert to milliseconds
                            
                            # Get calling function info
                            frame = inspect.currentframe()
                            while frame:
                                if frame.f_code.co_name == func.__name__:
                                    break
                                frame = frame.f_back
                            
                            source = source_name or f"{func.__module__}.{func.__name__}"
                            if frame:
                                source += f" (line {frame.f_lineno})"
                            
                            # Send response data to explorer service
                            request_data = {
                                "url": url,
                                "method": method_name,
                                "headers": headers,
                                "params": params,
                                "body": body,
                                "response_status": response.status_code,
                                "response_body": response.text,
                                "response_headers": dict(response.headers),
                                "duration_ms": duration,
                                "source": source
                            }
                            
                            # Log the complete request data
                            with httpx.Client() as client:
                                client.post(
                                    f"{self.explorer_url}/api/requests",
                                    json=request_data,
                                    timeout=2.0
                                )
                            
                            return response
                        except Exception as e:
                            # Log failed request
                            duration = (time.time() - start_time) * 1000
                            request_data = {
                                "url": url,
                                "method": method_name,
                                "headers": headers,
                                "params": params,
                                "body": body,
                                "response_status": 0,
                                "response_body": str(e),
                                "duration_ms": duration,
                                "source": source_name or f"{func.__module__}.{func.__name__}"
                            }
                            
                            try:
                                with httpx.Client() as client:
                                    client.post(
                                        f"{self.explorer_url}/api/requests",
                                        json=request_data,
                                        timeout=2.0
                                    )
                            except:
                                pass  # Ignore explorer service errors
                            
                            raise
                    
                    return intercepted_request
                
                # Patch request methods
                requests.get = create_interceptor(original_get, "GET")
                requests.post = create_interceptor(original_post, "POST")
                requests.put = create_interceptor(original_put, "PUT")
                requests.delete = create_interceptor(original_delete, "DELETE")
                requests.patch = create_interceptor(original_patch, "PATCH")
                
                try:
                    return func(*args, **kwargs)
                finally:
                    # Restore original methods
                    requests.get = original_get
                    requests.post = original_post
                    requests.put = original_put
                    requests.delete = original_delete
                    requests.patch = original_patch
            
            return wrapper
        return decorator 