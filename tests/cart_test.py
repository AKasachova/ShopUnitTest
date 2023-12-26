import pytest
from src.shop.cart import Cart
from src.shop.real_item import RealItem
from src.shop.virtual_item import VirtualItem

@pytest.fixture
def valid_cart_data():
    cart_name = "TestCart"
    return Cart(cart_name)


@pytest.mark.critical_workflow_smoke
def test_add_real_item(valid_cart_data, valid_real_item_data):
    valid_cart_data.add_real_item(valid_real_item_data)
    expected_total = valid_real_item_data.price + valid_real_item_data.price * Cart.TAX + Cart.DELIVERY_FEE * valid_real_item_data.weight
    assert valid_cart_data.total == expected_total, f"Unexpected total: {valid_cart_data.total}, Expected total: {expected_total}"


@pytest.mark.critical_workflow_smoke
def test_count_for_total_several_items(valid_cart_data, valid_real_item_data):
    virtual_items = [VirtualItem(name = "Microsoft office", price = 30.5, disk_size = 8500.0), VirtualItem(name = "Microsoft office", price = 35, disk_size = 9500.0)]
    valid_cart_data.add_real_item(valid_real_item_data)
    for item in virtual_items:
        valid_cart_data.add_virtual_item(item)
    assert valid_cart_data.total == 198.82999999999998, f"Unexpected total: {valid_cart_data.total}, Expected total: 198.829"
    