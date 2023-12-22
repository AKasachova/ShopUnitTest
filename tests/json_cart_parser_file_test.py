import pytest
from unittest.mock import mock_open, patch
from src.parser.json_cart_parser import read_from_file, write_to_file
from src.shop.cart import Cart
from src.shop.real_item import RealItem
from src.shop.virtual_item import VirtualItem

@pytest.fixture
def valid_json_data_zero_items():
    return '{"cart_name": "TestCart_0", "real_items": [], "virtual_items": [], "total": 0}'

@pytest.mark.positive_read
def test_read_from_file_zero_items(valid_json_data_zero_items):
    with patch("builtins.open", mock_open(read_data=valid_json_data_zero_items)):
        cart = read_from_file("test_file_path")
        assert cart.cart_name == "TestCart_0"
        assert cart.real_items == []
        assert cart.virtual_items == []
        assert cart.total == 0

@pytest.mark.positive_write
def test_write_to_file_zero_items(valid_json_data_zero_items):
    with patch("builtins.open", mock_open(read_data=valid_json_data_zero_items)) as mock_file:
        write_to_file(valid_json_data_zero_items, "test_file_path")
        mock_file.assert_called_once_with("test_file_path", "w")
        cart_read = read_from_file("test_file_path")
        assert cart_read.cart_name == "TestCart_0"
        assert cart_read.real_items == []
        assert cart_read.virtual_items == []
        assert cart_read.total == 0

@pytest.fixture
def valid_json_data_1real_item():
    return '{"cart_name": "TestCart_1", "real_items": [{"weight": 1.0, "name": "Toy", "price": 100.0}], "virtual_items": [], "total": 130.0}'

@pytest.mark.positive_read
def test_read_from_file_1real_item(valid_json_data_1real_item):
    with patch("builtins.open", mock_open(read_data=valid_json_data_1real_item)):
        cart = read_from_file("test_file_path")
        assert cart.cart_name == "TestCart_1"
        for item in cart.real_items:
            assert item.weight == 1.0
            assert item.name == "Toy"
            assert item.price == 100.0
            assert cart.virtual_items == []
            assert cart.total == 130.0

@pytest.mark.positive_write
def test_write_to_file_1real_item(valid_json_data_1real_item):
    with patch("builtins.open", mock_open(read_data=valid_json_data_1real_item)) as mock_file:
        write_to_file(valid_json_data_1real_item, "test_file_path")
        mock_file.assert_called_once_with("test_file_path", "w")
        cart_read = read_from_file("test_file_path")
        assert cart_read.cart_name == "TestCart_1"
        for item in cart_read.real_items:
            assert item.weight == 1.0
            assert item.name == "Toy"
            assert item.price == 100.0
        assert cart_read.virtual_items == []
        assert cart_read.total == 130.0

@pytest.fixture
def valid_json_data_1virtual_item():
    return '{"cart_name": "TestCart_2", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}], "total": 156.1}'

@pytest.mark.positive_read
def test_read_from_file_1virtual_item(valid_json_data_1virtual_item):
    with patch("builtins.open", mock_open(read_data=valid_json_data_1virtual_item)):
        cart = read_from_file("test_file_path")
        assert cart.cart_name == "TestCart_2"
        assert cart.real_items == []
        for item in cart.virtual_items:
            assert item.disk_size == 8500.0
            assert item.name == "Microsoft office"
            assert item.price == 30.0
        assert cart.total == 156.1

@pytest.mark.positive_write
def test_write_to_file(valid_json_data_1virtual_item):
    with patch("builtins.open", mock_open(read_data=valid_json_data_1virtual_item)) as mock_file:
        write_to_file(valid_json_data_1virtual_item, "test_file_path")
        mock_file.assert_called_once_with("test_file_path", "w")
        cart_read = read_from_file("test_file_path")
        assert cart_read.cart_name == "TestCart_2"
        assert cart_read.real_items == []
        for item in cart_read.virtual_items:
             assert item.disk_size == 8500.0
             assert item.name == "Microsoft office"
             assert item.price == 30.0
        assert cart_read.total == 156.1

@pytest.fixture
def valid_json_data_1real_1virtual_items():
    return '{"cart_name": "TestCart_3", "real_items": [{"weight": 2.0, "name": "Toy", "price": 100.3}], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}], "total": 297.1}'

@pytest.mark.critical_workflow_smoke
def test_read_from_file_1real_1virtual_items(valid_json_data_1real_1virtual_items):
    with patch("builtins.open", mock_open(read_data=valid_json_data_1real_1virtual_items)):
        cart = read_from_file("test_file_path")
        assert cart.cart_name == "TestCart_3"
        for item in cart.real_items:
            assert item.weight == 2.0
            assert item.name == "Toy"
            assert item.price == 100.3
        for item in cart.virtual_items:
            assert item.disk_size == 8500.0
            assert item.name == "Microsoft office"
            assert item.price == 30.0      
        assert cart.total == 297.1

@pytest.mark.critical_workflow_smoke
def test_write_to_file_1real_1virtual_items(valid_json_data_1real_1virtual_items):
    with patch("builtins.open", mock_open(read_data=valid_json_data_1real_1virtual_items)) as mock_file:
        write_to_file(valid_json_data_1real_1virtual_items, "test_file_path")
        mock_file.assert_called_once_with("test_file_path", "w")
        cart_read = read_from_file("test_file_path")
        assert cart_read.cart_name == "TestCart_3"
        for item in cart_read.real_items:
            assert item.weight == 2.0
            assert item.name == "Toy"
            assert item.price == 100.3
        for item in cart_read.virtual_items:
            assert item.disk_size == 8500.0
            assert item.name == "Microsoft office"
            assert item.price == 30.0      
        assert cart_read.total == 297.1

@pytest.fixture
def valid_json_data_2real_2virtual_items():
    return '{"cart_name": "TestCart_4", "real_items": [{"weight": 2.0, "name": "Toy", "price": 100.3}, {"weight": 1.1, "name": "Laptop", "price": 1002.3}], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}, {"disk_size": 9500.0, "name": "Microsoft office", "price": 35.6}], "total": 1200.1}'

@pytest.mark.positive_read
def test_read_from_file_2real_2virtual_items(valid_json_data_2real_2virtual_items):
    with patch("builtins.open", mock_open(read_data=valid_json_data_2real_2virtual_items)):
        cart = read_from_file("test_file_path")
        assert cart.cart_name == "TestCart_4"
        i = 0
        for item in cart.real_items:
            if i == 0:
                assert item.weight == 2.0
                assert item.name == "Toy"
                assert item.price == 100.3
            else:
                assert item.weight == 1.1
                assert item.name == "Laptop"
                assert item.price == 1002.3
            i += 1
        a = 0
        for item in cart.virtual_items:
            if a == 0:
                assert item.disk_size == 8500.0
                assert item.name == "Microsoft office"
                assert item.price == 30.0
            else:
                assert item.disk_size == 9500.0
                assert item.name == "Microsoft office"
                assert item.price == 35.6
            a += 1     
        assert cart.total == 1200.1

@pytest.mark.skip(reason = "There is no disk space to execute the test")
# @pytest.mark.positive_write
def test_write_to_file_2real_2virtual_items(valid_json_data_2real_2virtual_items):
    with patch("builtins.open", mock_open(read_data=valid_json_data_2real_2virtual_items)) as mock_file:
        write_to_file(valid_json_data_2real_2virtual_items, "test_file_path")
        mock_file.assert_called_once_with("test_file_path", "w")
        cart_read = read_from_file("test_file_path")
        assert cart_read.cart_name == "TestCart_4"
        i = 0
        for item in cart_read.real_items:
            if i == 0:
                assert item.weight == 2.0
                assert item.name == "Toy"
                assert item.price == 100.3
            else:
                assert item.weight == 1.1
                assert item.name == "Laptop"
                assert item.price == 1002.3
            i += 1
        a = 0
        for item in cart_read.virtual_items:
            if a == 0:
                assert item.disk_size == 8500.0
                assert item.name == "Microsoft office"
                assert item.price == 30.0
            else:
                assert item.disk_size == 9500.0
                assert item.name == "Microsoft office"
                assert item.price == 35.6
            a += 1     
        assert cart_read.total == 1200.1

@pytest.mark.parametrize("invalid_cart_data", [
        '{"invalid_cart_data"}',
        '{"invalid_key": "value"}',
        '{"cart_name": "TestCart",  "real_items": [] }',
        '{"cart_name": "TestCart",  "virtual_items": [] }',
        '{"cart_name": "TestCart", "real_items": [{"weight": 2.0, "name": "Toy"}], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [{"weight": 2.0, "price": 100.3}], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [ {"name": "Toy", "price": 100.3}],  "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office"}], "total": 1200.1]}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "price": 30.0}], "total": 1200.1]}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"name": "Microsoft office", "price": 30.0}], "total": 1200.1]}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}]}',
        '{"cart_name": "TestCart", "real_items": [{"weight": 2.0, "name": "Toy", "price": 100.3}, {"weight": 1.1, "name": "Laptop"}], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}, {"disk_size": 9500.0, "name": "Microsoft office"}], "total": 1200.1}',
        '{"cart_name": Test, "real_items": [], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": {"weight": "2.0", "name": "Toy", "price": 100.3}, "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": {"weight": 2.0, "name": Toy, "price": 100.3}, "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": {"weight": 2.0, "name": Toy, "price": "100.3"}, "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": {"disk_size": "8500.0", "name": "Microsoft office", "price": 30.0}, "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": {"disk_size": 8500.0, "name": Microsoft office, "price": 30.0}, "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": {"disk_size": 8500.0, "name": "Microsoft office", "price": "30.0"}, "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [], "total": test}',
])

@pytest.mark.negative_read
def test_read_from_file_exception(invalid_cart_data):
    with patch("builtins.open", mock_open(read_data=invalid_cart_data)):
        with pytest.raises(Exception):
            read_from_file("test_file_path")


@pytest.mark.parametrize("invalid_cart_data_write", [
        '{"invalid_cart_data"}',
        '{"invalid_key": "value"}',
        '{"cart_name": "TestCart",  "real_items": [] }',
        '{"cart_name": "TestCart",  "virtual_items": [] }',
        '{"cart_name": "TestCart", "real_items": [{"weight": 2.0, "name": "Toy"}], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [{"weight": 2.0, "price": 100.3}], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [ {"name": "Toy", "price": 100.3}],  "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office"}], "total": 1200.1]}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "price": 30.0}], "total": 1200.1]}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"name": "Microsoft office", "price": 30.0}], "total": 1200.1]}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}]}',
        '{"cart_name": "TestCart", "real_items": [{"weight": 2.0, "name": "Toy", "price": 100.3}, {"weight": 1.1, "name": "Laptop"}], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [{"disk_size": 8500.0, "name": "Microsoft office", "price": 30.0}, {"disk_size": 9500.0, "name": "Microsoft office"}], "total": 1200.1}',
        '{"cart_name": Test, "real_items": [], "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": {"weight": "2.0", "name": "Toy", "price": 100.3}, "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": {"weight": 2.0, "name": Toy, "price": 100.3}, "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": {"weight": 2.0, "name": Toy, "price": "100.3"}, "virtual_items": [], "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": {"disk_size": "8500.0", "name": "Microsoft office", "price": 30.0}, "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": {"disk_size": 8500.0, "name": Microsoft office, "price": 30.0}, "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": {"disk_size": 8500.0, "name": "Microsoft office", "price": "30.0"}, "total": 1200.1}',
        '{"cart_name": "TestCart", "real_items": [], "virtual_items": [], "total": test}',
])

@pytest.mark.negative_write
def test_write_to_file_exception(invalid_cart_data_write):
    with patch("builtins.open", mock_open(read_data=invalid_cart_data_write)) as mock_file:
        write_to_file(invalid_cart_data_write, "test_file_path")
        mock_file.assert_called_once_with("test_file_path", "w")
        with pytest.raises(Exception):
            read_from_file("test_file_path")
      


    

            
