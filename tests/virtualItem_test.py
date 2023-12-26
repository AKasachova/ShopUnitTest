import pytest
from src.shop.virtual_item import VirtualItem

@pytest.fixture
def invalid_param_data_virtual_item():
    name = 123
    price = 10.1
    disk_size = 1900
    return VirtualItem(name, price, disk_size)


@pytest.mark.negative_virtual_item
def test_missed_param_data_virtual_item_creation(invalid_param_data_virtual_item):
    with pytest.raises(TypeError):
        VirtualItem.to_str()
        