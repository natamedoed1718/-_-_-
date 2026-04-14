import pytest

from shop_pr.models import Category, CategoryIterator, Product


@pytest.fixture
def sample_products():
    return [
        Product("Phone", "Smartphone", 999.99, 10),
        Product("Laptop", "Gaming laptop", 1999.99, 5),
    ]


def test_product_init():
    product = Product("TV", "Smart TV", 500.0, 3)

    assert product.name == "TV"
    assert product.description == "Smart TV"
    assert product.price == 500.0
    assert product.quantity == 3


def test_category_init(sample_products):
    category = Category("Electronics", "Devices", sample_products)

    assert category.name == "Electronics"
    assert category.description == "Devices"
    assert len(category.products) == 2


def test_category_count(sample_products):
    Category.category_count = 0

    Category("Cat1", "Desc", sample_products)
    Category("Cat2", "Desc", sample_products)

    assert Category.category_count == 2


def test_product_count(sample_products):
    Category.product_count = 0

    Category("Cat1", "Desc", sample_products)
    Category("Cat2", "Desc", sample_products)

    assert Category.product_count == 4


def test_add_product():
    category = Category("Test", "Desc", [])
    product = Product("Test", "Desc", 100, 1)

    category.add_product(product)

    assert "Test" in category.products


def test_price_setter():
    product = Product("Test", "Desc", 100, 1)

    product.price = -10

    assert product.price == 100


def test_new_product():
    data = {
        "name": "Phone",
        "description": "Smartphone",
        "price": 1000,
        "quantity": 5,
    }

    product = Product.new_product(data)

    assert product.name == "Phone"


def test_product_str():
    product = Product("Phone", "Desc", 100, 2)

    assert str(product) == "Phone, 100 руб. Остаток: 2 шт."


def test_category_str(sample_products):
    category = Category("Electronics", "Desc", sample_products)

    assert str(category) == "Electronics, количество продуктов: 15 шт."


def test_product_add():
    p1 = Product("A", "Desc", 100, 10)
    p2 = Product("B", "Desc", 200, 2)

    assert p1 + p2 == 1400


def test_category_iterator(sample_products):
    category = Category("Test", "Desc", sample_products)

    iterator = CategoryIterator(category)

    products = [p for p in iterator]

    assert products == sample_products
