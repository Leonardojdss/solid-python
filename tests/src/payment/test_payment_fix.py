from src.payment.payment_pix import PaymentPIX
from src.order.order_delivery import OrderDelivery
from src.client import Client
from src.item import Item
import pytest

class TestPaymentPIX:
    def test_return_processing_payment_pix(self):
        """Test that PaymentPIX processes payment and returns correct amount"""
        
        # Given 
        expected_amount = "Processing PIX payment of R$: 19.50."
        client = Client("Leonardo", "123 Main St")
        item_1 = Item("Arroz", 9)
        tax_delivery = 10.5
        items = [item_1]
        order = OrderDelivery(client, items, tax_delivery)

        # When
        amount_order = order.calculate_total()
        payment_result = PaymentPIX().process_payment(amount_order)
        print(payment_result)

        # Then
        assert payment_result == expected_amount