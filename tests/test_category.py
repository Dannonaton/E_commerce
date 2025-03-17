import pytest
from src.category import Category


@pytest.fixture
def category_notebook():
    return Category("Apple", "Macbook Air", ["pro", "air"])


def test_init_category(category_notebook):
    assert category_notebook.name == "Apple"
    assert category_notebook.description == "Macbook Air"
    assert category_notebook.products == ["pro", "air"]
    assert category_notebook.product_count == 2
    assert Category.category_count == 1