from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, client_name, items):
        self.client_name = client_name
        self.items = items

    @abstractmethod
    def calculate_total(self):
        pass
