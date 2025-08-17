from src.client import Client
from src.item import Item
from src.order.order_delivery import OrderDelivery
from src.payment.payment_factory import PaymentFactory
from src.notification.notification_facade import NotificationFacade
from src.observer.observer_status import ObserverStatus

client = Client("Leonardo", "123 Main St")
item_1 = Item("Arroz", 9)
item_2 = Item("Carne", 30)
tax_delivery = 10.5
items = [item_1, item_2]

order = OrderDelivery(client, items, tax_delivery)
amount_order = order.calculate_total()
print(f"Preço total com delivery: {amount_order:.2f}")

# with strategy design
# Payment_card = PaymentCard().process_payment(amount_order)
# payment_pix = PaymentPIX().process_payment(amount_order)

# with factory design
type_payment = "cartao"
payment = PaymentFactory.create_payment(type_payment).process_payment(amount_order)

# MESSAGE = "Seu pedido saiu para entrega"
# Notify_email = NotificationEmail().send_notify(client, MESSAGE)
# Notify_sms = NotificationSMS().send_notify(client, MESSAGE)

MESSAGE_PAID = "You payment is confirmed"
MESSAGE_PREPARING = "You order is being prepared"
MESSAGE_ORDER_SEND = "You order is being sent"

notifications = NotificationFacade()
observer = ObserverStatus(notifications)
order.add_observers(observer)

order.status = MESSAGE_PAID
order.status = MESSAGE_PREPARING
order.status = MESSAGE_ORDER_SEND