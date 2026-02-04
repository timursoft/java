class NotificationService:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_match_found(self, player, opponent):
        for observer in self._observers:
            observer.update(player, opponent)