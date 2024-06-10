import pytest
from models import Product, Cart


@pytest.fixture(autouse=True)
def product_1():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture(autouse=True)
def product_2():
    return Product("box", 80, "This is a box", 600)


@pytest.fixture(autouse=True)
def cart():
    cart = Cart()
    return cart
