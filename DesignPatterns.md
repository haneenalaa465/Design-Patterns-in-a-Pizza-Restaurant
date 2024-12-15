# Design Patterns in the Pizza Restaurant System

## 1. Singleton Pattern: Inventory Manager

**Description:**
The Singleton pattern ensures that only one instance of the InventoryManager class exists. This instance is responsible for maintaining the inventory of pizzas and toppings.

**Usage in System:**
The InventoryManager prevents conflicting updates to the inventory and provides a centralized access point for inventory-related operations.

**Before Pattern Application:**
Without the Singleton pattern, multiple instances of the InventoryManager could lead to inconsistent inventory data.

**Benefits:**

- Centralized inventory management.

- Avoids data conflicts by ensuring a single source of truth.

## 2. Factory Method: Pizza Creation

**Description:**
The Factory Method encapsulates object creation logic, providing a single point for creating Margherita and Pepperoni pizzas.

**Usage in System:**
The PizzaFactory provides an easy way to create pizza objects without exposing their instantiation logic.

**Before Pattern Application:**
Pizza creation logic was scattered across the system, making it harder to add new pizza types.

**Benefits:**

- Simplifies pizza creation.

- Encourages consistency and scalability when adding new types.

## 3. Decorator Pattern: Adding Toppings

**Description:**
The Decorator pattern allows dynamic addition of toppings to a pizza object while maintaining the base pizza’s structure and behavior.

**Usage in System:**
Classes like CheeseTopping, OliveTopping, and MushroomTopping extend the base Pizza class functionality by appending to its description and cost.

**Before Pattern Application:**
Toppings were hard-coded into the pizza creation logic, limiting flexibility and reusability.

**Benefits:**

- Adds toppings dynamically at runtime.

- Supports composability for complex topping combinations.

## 4. Strategy Pattern: Payment Methods

**Description:**
The Strategy pattern encapsulates payment algorithms, providing a consistent interface for different payment methods.

**Usage in System:**
Classes like PayPalPayment and CreditCardPayment implement the PaymentMethod interface, enabling flexible payment processing.

**Before Pattern Application:**
Payment logic was directly tied to the order processing system, making it hard to extend or replace payment options.

**Benefits:**

- Decouples payment logic from order processing.

- Simplifies the addition of new payment methods.

## Concept of Overengineering

**Definition:**
Overengineering occurs when a system is designed with unnecessary complexity, often anticipating future requirements that may never materialize.

**Example of Overengineering in the Pizza System:**
If we added support for 20 different pizza types and 50 toppings using excessive abstraction layers (e.g., separate factories and decorators for each type), it would overcomplicate the system without immediate justification.

**Code Example:**
```
class CustomPizzaFactory:
    def create_custom_pizza(self, base_type: str, size: str, crust: str, toppings: list):
        # Overly complex pizza creation logic
        pizza = BasePizza(base_type, size, crust)
        for topping in toppings:
            pizza = ToppingDecoratorFactory.create_topping(pizza, topping)
        return pizza
```
**Why Overengineering is Problematic:**

- Reduces code readability.
- Increases maintenance overhead.
- Delays delivery by addressing non-essential features.

**Solution:**
Focus on current requirements, implementing additional complexity only when justified by evolving needs.
