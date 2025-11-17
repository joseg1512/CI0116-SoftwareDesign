from models.product import Product

class ProductDecorator(Product):
    
    def __init__(self, product: Product):
        self._product = product
    
    def get_description(self) -> str:
        return self._product.get_description()
    
    def get_price(self) -> float:
        return self._product.get_price()


class Milk(ProductDecorator):
    
    def get_description(self) -> str:
        return f"{self._product.get_description()} with milk"
    
    def get_price(self) -> float:
        return self._product.get_price() + 0.5


class Cinnamon(ProductDecorator):
    
    def get_description(self) -> str:
        return f"{self._product.get_description()} with cinnamon"
    
    def get_price(self) -> float:
        return self._product.get_price() + 0.3


class Cream(ProductDecorator):
    
    def get_description(self) -> str:
        return f"{self._product.get_description()} with cream"
    
    def get_price(self) -> float:
        return self._product.get_price() + 0.7


class ChocolateFilling(ProductDecorator):
    
    def get_description(self) -> str:
        return f"{self._product.get_description()} with chocolate filling"
    
    def get_price(self) -> float:
        return self._product.get_price() + 1.0


class Butter(ProductDecorator):
    
    def get_description(self) -> str:
        return f"{self._product.get_description()} with butter"
    
    def get_price(self) -> float:
        return self._product.get_price() + 0.4


class Honey(ProductDecorator):
    
    def get_description(self) -> str:
        return f"{self._product.get_description()} with honey"
    
    def get_price(self) -> float:
        return self._product.get_price() + 0.6
