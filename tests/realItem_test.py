import pytest
from src.shop.real_item import RealItem

@pytest.fixture
def valid_real_item_data():
    name = "Toy"
    price = 10.1
    weight = 1.1
    return RealItem(name, price, weight)


@pytest.mark.critical_workflow_smoke
def test_real_item_creation(valid_real_item_data):
    assert isinstance(valid_real_item_data, RealItem)
    assert valid_real_item_data.name == "Toy"
    assert valid_real_item_data.price == 10.1
    assert valid_real_item_data.weight == 1.1


def test_string_method(valid_real_item_data):
    assert valid_real_item_data.to_str() == "Real Item: Toy, price: 10.1, weight: 1.1;"