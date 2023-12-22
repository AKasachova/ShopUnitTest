import json
from json import JSONEncoder
from types import SimpleNamespace

from src.shop.cart import Cart
from src.shop.real_item import RealItem
from src.shop.virtual_item import VirtualItem


def read_from_file(path) -> Cart:
    with open(path) as file:
        file_content = file.read()

    parsed_json = json.loads(file_content, object_hook=lambda d: SimpleNamespace(**d))

    cart = Cart(parsed_json.cart_name)
    cart.total = parsed_json.total
    cart.real_items = [RealItem(item.name, item.price, item.weight) for item in parsed_json.real_items]
    cart.virtual_items = [VirtualItem(item.name, item.price, item.disk_size) for item in parsed_json.virtual_items]

    return cart


def write_to_file(cart, path) -> None:
    with open(path, "w") as file:
        json.dump(cart, file, cls=CartEncoder)


class CartEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
