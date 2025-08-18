import pytest
from src.item import Item

def test_item_initialization():
    item = Item("Book", 12.99)
    assert item.name == "Book"
    assert item.price == 12.99

@pytest.mark.parametrize("name, price", [
    ("Pen", 1.5),
    ("Notebook", 5.0),
    ("Eraser", 0.99),
])
def test_item_multiple_initializations(name, price):
    item = Item(name, price)
    assert item.name == name
    assert item.price == price