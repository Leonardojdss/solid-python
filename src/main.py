from src.client import Client
from src.item import Item
from src.order.order_collected import OrderCollected
from src.order.order_delivery import OrderDelivery
# from src.payment.payment_card import PaymentCard
# from src.payment.payment_pix import PaymentPIX
from src.payment.payment_factory import PaymentFactory

client = Client("Leonardo", "123 Main St")
item_1 = Item("Arroz", 9)
item_2 = Item("Carne", 30)
tax_delivery = 10.5
items = [item_1, item_2]

order_collected = OrderCollected(client, items)
order_delivery = OrderDelivery(client, items, tax_delivery)
amount_order = order_delivery.calculate_total()
print(f"Preço total: {order_collected.calculate_total():.2f}")
print(f"Preço total com delivery: {amount_order:.2f}")

# with strategy design
# Payment_card = PaymentCard().process_payment(amount_order)
# payment_pix = PaymentPIX().process_payment(amount_order)

# with factory design
type_payment = "cartao"
payment = PaymentFactory.create_payment(type_payment).process_payment(amount_order)