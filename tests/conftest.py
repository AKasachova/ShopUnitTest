import pytest
from src.shop.real_item import RealItem

@pytest.fixture
def valid_real_item_data():
    name = "Toy"
    price = 100.1
    weight = 1.1
    return RealItem(name, price, weight)
