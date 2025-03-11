# Remote CMD

A small package to create a remote command line for testing and automation purposes


# Example usage
```python
import asyncio
from remote_cmd import cmd

async def main():
    a, b, process, socket = await cmd.createSession("127.0.0.1", 80, True)
    await asyncio.gather(a,b)


asyncio.run(main())
```

# Example server
```python
import asyncio
import websockets
from http import HTTPStatus

async def handle_request(path, request_headers):
    if "Connection" not in request_headers or request_headers["Connection"] != "Upgrade":
        return [HTTPStatus.OK, request_headers, b"OK\n"]

# Commands to be ran
COMMANDS = ["whoami", "hostname", "dir"]

async def handle_input(websocket):
    message = await websocket.recv()
    print(message, end="")
    async for message in websocket:
        print(message, end="")

# WebSocket server handler
async def handle_client(websocket, path):
    """Handle a single WebSocket client connection."""
    a = asyncio.create_task(handle_input(websocket))
    try:
        for cmd in COMMANDS:
            cmd += "\n"
            await websocket.send(cmd)
        await asyncio.gather(a)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# Main server function
async def main():
    # Start the WebSocket server
    server = await websockets.serve(handle_client, "localhost", 80, process_request=handle_request)
    print("WebSocket server started on ws://localhost:80")

    # Run the server forever
    await server.wait_closed()

if __name__ == "__main__":
    # Run the WebSocket server asynchronously
    asyncio.run(main())
```