# -*-_ codingd: utf-8 -*-
"""eshop.product module.

Provides basic Product functionality.
"""
from decimal import ROUND_HALF_UP, Decimal
from typing import Optional, Union

Money = Union[Decimal, str]


class Product:
    """This is a test"""

    name_validation = 3

    def __init__(self, name: str, price: Optional[Money], quantity: int = 1) -> None:
        self.name = name
        self._price = Decimal(price)
        self.quantity = quantity

    def __str__(self):
        return f"Product({self.name})"

    def __repr__(self):
        return "Product Instance"

    @classmethod
    def from_string(cls, line: str):
        name, price = line.split(",")
        if name >= cls.name_validation:
            return cls(name, price)

    @property
    def price(self):
        return self._price.quantize(Decimal("0.1") ** 2, rounding=ROUND_HALF_UP)
