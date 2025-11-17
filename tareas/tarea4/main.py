from app.cafeteria import Cafeteria
from models.base_products import Coffee, Croissant, GreenTea, Muffin
from models.decorators import Milk, Cinnamon, ChocolateFilling, Cream, Honey


def main():
    print("Cafeteria")
    
    cafeteria = Cafeteria()
    
    print("\nCustomer: Ana")
    ana = cafeteria.register_customer("Ana")
    ana_order = cafeteria.create_order(ana)
    
    coffee_ana = Cinnamon(Milk(Coffee()))
    print(f"Orders: {coffee_ana.get_description()}")
    ana_order.add_product(coffee_ana)
    
    croissant_ana = ChocolateFilling(Croissant())
    print(f"Orders: {croissant_ana.get_description()}")
    ana_order.add_product(croissant_ana)
    
    print("\nCustomer: Carlos")
    carlos = cafeteria.register_customer("Carlos")
    carlos_order = cafeteria.create_order(carlos)
    
    tea_carlos = Honey(GreenTea())
    print(f"Orders: {tea_carlos.get_description()}")
    carlos_order.add_product(tea_carlos)
    
    muffin_carlos = Cream(Muffin())
    print(f"Orders: {muffin_carlos.get_description()}")
    carlos_order.add_product(muffin_carlos)
    
    print("\nPROCESSING ORDERS")
    
    cafeteria.process_order(ana_order)
    cafeteria.process_order(carlos_order)

if __name__ == "__main__":
    main()
