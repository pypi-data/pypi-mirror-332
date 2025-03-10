# HTTP Request Catcher

A Python library for capturing and mocking HTTP requests made with the `requests` library.

## Features

- Capture all HTTP requests made with the `requests` library
- Track request/response headers, bodies, timing, and more
- Track request source (function name and line number)
- Support for request mocking
- Zero configuration required
- Minimal impact on application performance

## Installation

```bash
pip install catchttp
```

## Usage

```python
from catchttp import RequestCatcher
import requests

# Initialize the catcher with your explorer service URL
catcher = RequestCatcher("http://localhost:8000")

# Add the decorator to functions that make HTTP requests
@catcher.catch_requests("my_service")
def fetch_data():
    response = requests.get("https://api.example.com/data")
    return response.json()
```

## Explorer Service

The request explorer service (with UI for exploring captured requests) is available as a separate Docker image. 
You can find it at [catchttp-explorer](https://github.com/nikolai/catchttp-explorer).

## Configuration

### Request Catcher

- `explorer_url`: URL of your explorer service (default: "http://localhost:8000")
- `source_name`: Custom name for the request source (optional)

## Development

The project structure:

```
.
├── request_catcher/
│   ├── __init__.py
│   └── decorator.py
├── example.py
├── requirements.txt
└── README.md
```

## License

MIT License 