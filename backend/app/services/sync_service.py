from typing import Dict, Any
from loguru import logger
from backend.app.utils.observer import Observer, Subject
from backend.app.utils.websocket_manager import WebSocketManager
from backend.app.models.game_state import GameState

class SyncService(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.websocket_manager = WebSocketManager()

    def update_progress(self, game_state: GameState) -> None:
        """
        Update the game progress and notify all observers (clients).
        """
        try:
            self.notify_observers(game_state)
            self.websocket_manager.broadcast(game_state)
            logger.info("Game progress updated and broadcasted successfully.")
        except Exception as e:
            logger.error("Failed to update game progress: {}", e)

    def notify_observers(self, game_state: GameState) -> None:
        for observer in self.observers:
            observer.update(game_state)

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)