from src.order.order import Order

class OrderCollected(Order):

    def calculate_total(self):
        return sum(item.price for item in self.items)