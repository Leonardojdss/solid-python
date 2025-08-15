from src.payment.payment_card import PaymentCard
from src.payment.payment_pix import PaymentPIX

class PaymentFactory:
    @staticmethod
    def create_payment(type):
        if type == "pix":
            return PaymentPIX()
        elif type == "cartao":
            return PaymentCard()
        else:
            raise ValueError(f"tipo de pagamento '{type}' não suportado")