import pytest
from src.product import Product


@pytest.fixture
def product_macbook():
    return Product("Apple", "Macbook Air", 60000, 20)


def test_init_product(product_macbook):
    assert product_macbook.name == "Apple"
    assert product_macbook.description == "Macbook Air"
    assert product_macbook.price == 60000
    assert product_macbook.quantity == 20