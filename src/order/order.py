from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, client_name, items):
        self.client_name = client_name
        self.items = items
        self._status = "created"
        self.observers = []

    # Getter
    @property
    def status(self):
        return self._status
    
    # Setter
    @status.setter
    def status(self, new_status):
        self._status = new_status
        self.notify_observers()

    def add_observers(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_status(self)

    @abstractmethod
    def calculate_total(self):
        pass