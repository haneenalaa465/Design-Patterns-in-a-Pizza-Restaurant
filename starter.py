from abc import ABC, abstractmethod

# Singleton: Inventory Manager
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryManager, cls).__new__(cls)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

# Factory Method: Pizza Creation
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

class MargheritaPizza(Pizza):
    def get_description(self) -> str:
        return "Margherita"

    def get_cost(self) -> float:
        return 5.0

class PepperoniPizza(Pizza):
    def get_description(self) -> str:
        return "Pepperoni"

    def get_cost(self) -> float:
        return 6.0

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type")

# Decorator: Add Toppings Dynamically
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

class CheeseTopping(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + " + Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0

class OliveTopping(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + " + Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.5

class MushroomTopping(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + " + Mushrooms"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.7

# Strategy: Payment Method
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using PayPal. Payment successful!")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Paid ${amount:.2f} using Credit Card. Payment successful!")

# --- Main Program ---
def main():
    inventory_manager = InventoryManager()
    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0. Exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == '0':
            break

        if pizza_choice == '1' and inventory_manager.check_and_decrement("Margherita"):
            pizza = PizzaFactory.create_pizza("Margherita")
        elif pizza_choice == '2' and inventory_manager.check_and_decrement("Pepperoni"):
            pizza = PizzaFactory.create_pizza("Pepperoni")
        else:
            print("Base pizza unavailable or out of stock!")
            continue

        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == '1' and inventory_manager.check_and_decrement("Cheese"):
                pizza = CheeseTopping(pizza)
            elif topping_choice == '2' and inventory_manager.check_and_decrement("Olives"):
                pizza = OliveTopping(pizza)
            elif topping_choice == '3' and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = MushroomTopping(pizza)
            elif topping_choice == '4':
                break
            else:
                print("Topping unavailable or out of stock!")

        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == '1':
            payment_method = PayPalPayment()
        elif payment_choice == '2':
            payment_method = CreditCardPayment()
        else:
            print("Invalid payment method!")
            continue

        payment_method.pay(pizza.get_cost())

        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())

if __name__ == "__main__":
    main()
