from src.payment.payment import Payment

class PaymentCard(Payment):

    def process_payment(self, amount):
        print(f"Processing card payment of R$: {amount:.2f}.")