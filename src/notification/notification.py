from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification(self, client_name, message):
        pass

