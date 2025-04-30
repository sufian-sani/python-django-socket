# import asyncio
# import websockets

# # This is the WebSocket server handler that will receive and echo back the messages
# async def echo(websocket):  # Make sure to accept the `path` argument
#     print(f"New connection with path:")
    
#     try:
#         # Wait for a message from the sender
#         async for message in websocket:
#             print(f"Received message: {message}")
#             # Send the received message back to the sender
#             await websocket.send(f"Received: {message}")
#     except websockets.exceptions.ConnectionClosed as e:
#         print(f"Connection closed: {e}")

# # Start the WebSocket server
# async def main():
#     start_server = await websockets.serve(echo, "127.0.0.1", 8000)
#     print("WebSocket server started at ws://127.0.0.1:8000")
#     await asyncio.Future()  # Run the server indefinitely

# # Run the event loop and start the server
# if __name__ == "__main__":
#     asyncio.run(main())

# -----------------------base 1 -----------------
# import asyncio
# import websockets

# async def hello(websocket):
#     name = await websocket.recv()
#     print(f'Server Received: {name}')
#     greeting = f'Hello {name}!'

#     await websocket.send(greeting)
#     print(f'Server sent: {greeting}')

# async def main():
#     async with websockets.serve(hello, "localhost",8765):
#         await asyncio.Future()

# if __name__ == "__main__":
#     asyncio.run(main())
# -----------------------base 2 -----------------

# websocket_server.py
# websocket_server.py
import asyncio
import websockets
import threading

async def handle_connection(websocket):
    async def receive():
        async for message in websocket:
            print(f"\nClient: {message}")

    async def send():
        loop = asyncio.get_event_loop()
        while True:
            msg = await loop.run_in_executor(None, input, "You (Server): ")
            await websocket.send(msg)

    await asyncio.gather(receive(), send())

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Server started at ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

