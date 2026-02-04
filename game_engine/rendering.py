from loguru import logger

class Event:
    subscribers = {}

    @classmethod
    def subscribe(cls, event_type: str, callback):
        if event_type not in cls.subscribers:
            cls.subscribers[event_type] = []
        cls.subscribers[event_type].append(callback)

    @classmethod
    def trigger(cls, event_type: str, **kwargs):
        if event_type in cls.subscribers:
            for callback in cls.subscribers[event_type]:
                try:
                    callback(**kwargs)
                except Exception as e:
                    logger.error("Error during event {} handling: {}", event_type, e)

class Renderer:
    def __init__(self):
        Event.subscribe('collision', self.show_collision_effect)

    def show_collision_effect(self, position: tuple[int, int]) -> None:
        logger.info("Showing collision effect at position: {}", position)
        # Here, implement the visual effect logic
        pass