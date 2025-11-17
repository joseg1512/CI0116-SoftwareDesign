from typing import Dict
from app.customer import Customer
from app.order import Order
from models.product import Product

class Cafeteria:
    
    def __init__(self):
        self._customers: Dict[str, Customer] = {}
        self._orders: list[Order] = []
        self._current_order_number = 1
    
    def register_customer(self, name: str) -> Customer:
        if name not in self._customers:
            self._customers[name] = Customer(name)
        return self._customers[name]
    
    def create_order(self, customer: Customer) -> Order:
        order = Order(self._current_order_number)
        order.attach(customer)
        self._orders.append(order)
        self._current_order_number += 1
        return order
    
    def process_order(self, order: Order) -> None:
        order.prepare()
        print(f"  Total: ${order.calculate_total():.2f}")
        order.mark_ready()
