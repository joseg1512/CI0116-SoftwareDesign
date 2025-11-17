from typing import List
from models.product import Product
from observers.subject import Subject

class OrderStatus:
    PENDING = "Pending"
    IN_PROGRESS = "In progress"
    READY = "Ready"
    DELIVERED = "Delivered"

class Order(Subject):
    
    def __init__(self, number: int):
        super().__init__()
        self._number = number
        self._products: List[Product] = []
        self._status = OrderStatus.PENDING
    
    @property
    def number(self) -> int:
        return self._number
    
    @property
    def status(self) -> str:
        return self._status
    
    def add_product(self, product: Product) -> None:
        self._products.append(product)
    
    def get_products(self) -> List[Product]:
        return self._products.copy()
    
    def calculate_total(self) -> float:
        return sum(product.get_price() for product in self._products)
    
    def change_status(self, new_status: str) -> None:
        self._status = new_status
        if self._status == OrderStatus.READY:
            self.notify()
    
    def prepare(self) -> None:
        self.change_status(OrderStatus.IN_PROGRESS)
        print(f"Preparing order #{self._number}...")
        for i, product in enumerate(self._products, 1):
            print(f"  {i}. {product.get_description()} - ${product.get_price():.2f}")
    
    def mark_ready(self) -> None:
        self.change_status(OrderStatus.READY)
