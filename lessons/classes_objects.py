"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute definitions
    size: str
    toppings: int
    extra_cheese: bool

    
def price(pizza: Pizza) -> float:
    """Calculate the price of a Pizza"""
    total: float = 0.0
    # TODO -- compute prrice
    return total


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)