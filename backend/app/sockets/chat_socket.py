from fastapi import WebSocket, WebSocketDisconnect
from fastapi_websocket_pubsub import PubSubEndpoint
from typing import List
from backend.app.models.chat_message import ChatMessage

class ChatSocket:
    def __init__(self):
        self.endpoint = PubSubEndpoint()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.endpoint.add_subscriber(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.endpoint.remove_subscriber(websocket)

    async def send_message(self, message: dict):
        await self.endpoint.publish(message)

    async def handle_messages(self, websocket: WebSocket):
        try:
            while True:
                data = await websocket.receive_json()
                if 'send_message' in data:
                    message = ChatMessage.create_from_dict(data['send_message'])
                    await self.send_message({'receive_message': message.to_dict()})
        except WebSocketDisconnect:
            await self.disconnect(websocket)
