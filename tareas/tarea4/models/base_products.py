from models.product import Product

class Coffee(Product):
    
    def get_description(self) -> str:
        return "Coffee"
    
    def get_price(self) -> float:
        return 2.5


class Tea(Product):
    
    def get_description(self) -> str:
        return "Tea"
    
    def get_price(self) -> float:
        return 2.0


class GreenTea(Product):
    
    def get_description(self) -> str:
        return "Green tea"
    
    def get_price(self) -> float:
        return 2.3


class Croissant(Product):
    
    def get_description(self) -> str:
        return "Croissant"
    
    def get_price(self) -> float:
        return 3.0


class Toast(Product):
    
    def get_description(self) -> str:
        return "Toast"
    
    def get_price(self) -> float:
        return 2.5


class Muffin(Product):
    
    def get_description(self) -> str:
        return "Muffin"
    
    def get_price(self) -> float:
        return 3.5
