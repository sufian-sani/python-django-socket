# import asyncio
# import websockets

# async def send_message():
#     uri = "ws://127.0.0.1:8000"
    
#     async with websockets.connect(uri) as websocket:
#         message = "Hello, WebSocket Server send from client server------------!"
#         # print(f"Sending message: {message}")
#         await websocket.send(message)
        
#         response = await websocket.recv()
#         breakpoint()
#         print(f"Received response: {response}")

# asyncio.get_event_loop().run_until_complete(send_message())

# -----------------------base 1 -----------------

# import asyncio
# import websockets

# async def hello():
#     uri = "ws://localhost:8765"
#     async with websockets.connect(uri) as websocket:
#         name = input("What's your name? ")

#         await websocket.send(name)
#         print(f'Client sent: {name}')

#         greeting = await websocket.recv()
#         print(f"client received: {greeting}")

# if __name__ == "__main__":
#     asyncio.run(hello())

# -----------------------base 2 -----------------
# websocket_client.py
# websocket_client.py
import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:

        async def receive():
            async for message in websocket:
                print(f"\nServer: {message}")

        async def send():
            loop = asyncio.get_event_loop()
            while True:
                msg = await loop.run_in_executor(None, input, "You (Client): ")
                await websocket.send(msg)

        await asyncio.gather(receive(), send())

if __name__ == "__main__":
    asyncio.run(chat_client())
