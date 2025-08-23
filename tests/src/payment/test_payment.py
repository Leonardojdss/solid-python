from src.payment.payment import Payment
import pytest

def test_cannot_instantiate_payment():
    with pytest.raises(TypeError):
        Payment()

def test_subclass_without_process_payment():
    class IncompletePayment(Payment):
        pass

    with pytest.raises(TypeError):
        IncompletePayment()