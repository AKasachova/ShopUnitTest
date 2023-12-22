
class Cart:
    TAX = 0.2
    DELIVERY_FEE = 0.1

    def __init__(self, cart_name: str):
        self.cart_name = cart_name
        self.total = 0.0
        self.real_items = []
        self.virtual_items = []

    def add_real_item(self, item) -> None:
        self.real_items.append(item)
        self.total += item.price + item.price * Cart.TAX + Cart.DELIVERY_FEE * item.weight
        print(f'{self.total}')
        
    def add_virtual_item(self, item) -> None:
        self.virtual_items.append(item)
        self.total += item.price + item.price * Cart.TAX

    def show_all_items(self) -> None:
        print(f"Cart {self.cart_name}:")
        print(*[item.name for item in self.real_items], *[item.name for item in self.virtual_items], sep=", ")

    def get_total_price(self) -> float:
        print(f"Cart {self.cart_name} total value: {self.total}")

        return self.total
