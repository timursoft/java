from websockets import serve
from backend.app.models.game_state import GameState
from loguru import logger

class SyncService:
    def __init__(self):
        self.clients = set()

    async def register(self, websocket):
        self.clients.add(websocket)
        logger.info("Client registered: {}", websocket.remote_address)

    async def unregister(self, websocket):
        self.clients.remove(websocket)
        logger.info("Client unregistered: {}", websocket.remote_address)

    async def notify_clients(self, message: str):
        if self.clients:  # Check if there are any clients connected
            await asyncio.wait([client.send(message) for client in self.clients])
            logger.info("Broadcast message: {}", message)

    async def broadcast_game_state(self, game_state: GameState):
        message = game_state.to_json()
        await self.notify_clients(message)
        logger.debug("Broadcasted game state: {}", message)

    async def handler(self, websocket, path):
        await self.register(websocket)
        try:
            async for message in websocket:
                pass  # For now, we are only broadcasting
        finally:
            await self.unregister(websocket)

sync_service = SyncService()