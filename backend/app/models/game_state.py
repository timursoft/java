from typing import Callable, List

class GameState:
    def __init__(self):
        self._observers: List[Callable[[str], None]] = []

    def add_observer(self, observer: Callable[[str], None]) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Callable[[str], None]) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer(self.to_json())

    def update_state(self, new_state_data: dict) -> None:
        # Update game state logic
        self.notify_observers()

    def to_json(self) -> str:
        # Convert game state to JSON
        return "{}"
