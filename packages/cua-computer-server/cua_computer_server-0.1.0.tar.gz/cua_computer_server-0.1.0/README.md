# CUA Computer API

The API server component of the Computer Universal Automation (CUA) project. It provides WebSocket endpoints for interacting with the computer control functionality.

## Features

- WebSocket API for computer control
- Cross-platform support (macOS, Linux)
- Integration with CUA computer library for screen control, keyboard/mouse automation, and accessibility

## Installation

### From Source

```bash
cd server/computer-api
pip install -e .
```

### As a Dependency

```bash
pip install cua-computer-api
```

## Usage

### Command Line

After installation, you can run the server from the command line:

```bash
# Run with default settings (host=0.0.0.0, port=8000)
cua-computer-api

# Run with custom settings
cua-computer-api --host 127.0.0.1 --port 8080 --log-level debug
```

### As an Imported Package

The server can be used programmatically in your own code:

```python
# Synchronous usage
from computer_api import Server

server = Server(port=8080)
server.start()  # Blocks until stopped
```

```python
# Asynchronous usage
import asyncio
from computer_api import Server

async def main():
    server = Server(port=8080)
    
    # Start server in background
    await server.start_async()
    
    # Do other work while server is running
    await asyncio.sleep(10)
    
    # Stop the server
    await server.stop()

asyncio.run(main())
```

See the `examples` directory for more detailed usage examples.

## Development

To run the server in development mode:

```bash
# Using PDM
pdm run api

# Or directly
python -m computer_api
```

## License

MIT License 