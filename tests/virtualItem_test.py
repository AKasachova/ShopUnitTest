import pytest
from src.shop.virtual_item import VirtualItem

@pytest.fixture
def invalid_param_data_virtual_item():
    name = 'Test123'
    price = 10.1
    disk_size = 1900
    return VirtualItem(name, price, disk_size)


@pytest.mark.negative_virtual_item
def test_incorrect_param_data_virtual_item_to_str(invalid_param_data_virtual_item):
    assert invalid_param_data_virtual_item.to_str() == "Virtual Item: Test123, price: 10.1, disk_size: 1900;", f"Incorrect VirtualItem class attribute"
