from src.shop.item import Item


class VirtualItem(Item):
    def __init__(self, name, price, disk_size):
        super().__init__(name, price)
        self.disk_size = disk_size

    def to_str(self):
        return f"Virtual Item: {self.name}, price: {self.price}, disk_size: {self.disk_size};"
