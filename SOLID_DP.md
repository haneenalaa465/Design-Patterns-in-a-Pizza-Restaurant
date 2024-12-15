# Design Patterns and Their Relation to SOLID Principles

## 1. Singleton Pattern: Inventory Manager

**Description:**
The `InventoryManager` class implements the Singleton pattern to ensure there is only one instance managing the inventory.

**Adheres to SOLID Principles:**

- **Single Responsibility Principle (SRP):** The class is solely responsible for managing the inventory's state and operations.

- **Dependency Inversion Principle (DIP):** High-level modules like the main program depend on the `InventoryManager` abstraction rather than directly manipulating inventory data.

## 2. Factory Method: Pizza Creation

**Description:**
The `PizzaFactory` class encapsulates the logic for creating different types of pizzas (`Margherita` or `Pepperoni`).

**Adheres to SOLID Principles:**

- **Open/Closed Principle (OCP):** New pizza types can be added without modifying the existing factory logic.

- **Single Responsibility Principle (SRP):** The factory is dedicated solely to object creation.

## 3. Decorator Pattern: Adding Toppings

**Description:**
The `ToppingDecorator` class and its subclasses (`CheeseTopping`, `OliveTopping`, and `MushroomTopping`) dynamically add functionalities (toppings) to a pizza object without altering the base class.

**Adheres to SOLID Principles:**

- **Open/Closed Principle (OCP):** New toppings can be added without modifying the existing classes.

- **Liskov Substitution Principle (LSP):** All decorators conform to the base `Pizza` class interface, ensuring substitutability.

## 4. Strategy Pattern: Payment Methods

**Description:**
The `PaymentMethod` interface defines a family of payment strategies (`PayPalPayment` and `CreditCardPayment`).

**Adheres to SOLID Principles:**

- **Open/Closed Principle (OCP):** New payment methods can be introduced without altering existing code.

- **Interface Segregation Principle (ISP):** Each payment method class adheres to a minimal interface, focusing solely on payment execution.

- **Dependency Inversion Principle (DIP):** High-level modules depend on the `PaymentMethod` abstraction rather than concrete payment implementations.
