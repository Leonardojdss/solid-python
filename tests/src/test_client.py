from src.client import Client
import pytest

def test_client_initialization():
    client = Client("Leonardo", "rua generative AI")
    assert client.name == "Leonardo"
    assert client.address == "rua generative AI"

@pytest.mark.parametrize("name, adrress",
    [("Leonardo_01", "rua generative ai 1"),
     ("Leonardo_02", "rua generative ai 2"),
     ("Leonardo_03", "rua generative ai 3")]
)
def test_client_multiple_initializations(name, adrress):
    client = Client(name, adrress)
    assert client.name == name
    assert client.address == adrress