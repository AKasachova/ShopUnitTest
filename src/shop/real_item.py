from src.shop.item import Item


class RealItem(Item):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def to_str(self):
        return f"Real Item: {self.name}, price: {self.price}, weight: {self.weight};"
