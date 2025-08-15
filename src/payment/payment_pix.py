from src.payment.payment import Payment

class PaymentPIX(Payment):

    def process_payment(self, amount):
        print(f"Processing PIX payment of R$: {amount:.2f}.")