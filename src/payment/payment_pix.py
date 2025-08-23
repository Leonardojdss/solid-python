from src.payment.payment import Payment

class PaymentPIX(Payment):

    def process_payment(self, amount):
        RETURN_AMOUNT = f"Processing PIX payment of R$: {amount:.2f}."
        print(RETURN_AMOUNT)
        return RETURN_AMOUNT