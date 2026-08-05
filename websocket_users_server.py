import asyncio

import websockets
from websockets import ServerConnection

async def echo(websocket:ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for index in range (5):
            response = f"{index+1} Сообщение от пользователя: {message}"
            await websocket.send(response)

async def main():
    server=await websockets.serve(echo,'localhost',8765)
##  print(f"WebSocket запущен на адрес ws://localhost:{8765}")
    await server.wait_closed()

asyncio.run(main())
