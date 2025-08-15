from src.order.order import Order

class OrderDelivery(Order):
    def __init__(self, client_name, items, tax_delivery):
        super().__init__(client_name, items)
        self.tax_delivery = tax_delivery

    def calculate_total(self):
        total = sum(item.price for item in self.items) + self.tax_delivery
        return total