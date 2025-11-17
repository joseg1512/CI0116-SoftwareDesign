from observers.observer import Observer
from observers.subject import Subject

class Customer(Observer):
    
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    def update(self, subject: Subject) -> None:
        from app.order import Order
        if isinstance(subject, Order):
            print(f"Notification for {self._name}: Your order is ready")
