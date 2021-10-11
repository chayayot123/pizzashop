from pizza import *


# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should


def order_pizza(pizza: Pizza):
    print(f"A {str(pizza)}")
    print("Price:", pizza.get_price())


if __name__ == "__main__":
    pizza = Pizza(PizzaSize.small)
    pizza.add_topping("mushroom")
    pizza.add_topping("tomato")
    pizza.add_topping("pineapple")
    order_pizza(pizza)

    # a plain pizza
    pizza2 = Pizza(PizzaSize.medium)
    order_pizza(pizza2)

    # pizza with only one topping
    pizza3 = Pizza(PizzaSize.large)
    pizza3.add_topping("seafood")
    order_pizza(pizza3)

    pizza4 = Pizza(PizzaSize.jumbo)
    pizza4.add_topping("cheese")
    order_pizza(pizza4)
