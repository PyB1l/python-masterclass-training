# -*-coding: utf-8 -*-
"""`eshop.cart` module

Provides Eshop Cart base classes and functionality.
"""

from typing import List

from product import Product


class Cart:
    """This is a best way of handling them all.

    Attributes:
        items (list): A list of Product instances.
    """

    def __init__(self, items: List[Product]) -> None:
        """This is a test for the ppython intepreter"""
        self._items = items
        self._pricing = [
            "a",
            "b",
        ]

    @property
    def price(self):
        return (
            "free"
            if not len(self._items)
            else sum(product.price for product in self._items)
        )


if __name__ == "__main__":

    items = [
        Product(name="Shoes", quantity=1, price="12.09"),
        Product(name="T-SHirt", quantity=2, price="9.99"),
    ]

    cart = Cart(items=items)

    print(cart.price)
