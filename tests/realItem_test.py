import pytest
from src.shop.real_item import RealItem

@pytest.mark.critical_workflow_smoke
def test_real_item_creation(valid_real_item_data):
    assert isinstance(valid_real_item_data, RealItem)
    assert valid_real_item_data.name == "Toy"
    assert valid_real_item_data.price == 100.1
    assert valid_real_item_data.weight == 1.1
