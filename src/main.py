from src.shop.cart import Cart
from src.parser.json_cart_parser import write_to_file, read_from_file
from src.shop.real_item import RealItem
from src.shop.virtual_item import VirtualItem

phone = RealItem("Phone", 1000, 0.2)
netflix = VirtualItem("Netfix subscription", 80, 1000)
windows = VirtualItem("MS Windows", 100, 10000000)

cart = Cart("Jon")
cart.add_real_item(phone)
cart.add_virtual_item(netflix)
cart.add_virtual_item(windows)
cart.show_all_items()
cart.get_total_price()

write_to_file(cart, "data.json")

json_cart = read_from_file("default_cart.json")
json_cart.show_all_items()

if __name__ == '__main__':
    pass
