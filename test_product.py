import pytest
from products import Product, InventoryError, NonStockedProduct, LimitedProduct


def test_product_creation_successful():
    product = Product("Laptop", 250.0, 100)
    assert product.name == "Laptop"
    assert product.price == 250.0
    assert product.quantity == 100
    assert product.is_active() is True


def test_empty_name_exception():
    with pytest.raises(ValueError) as exc_info:
        Product("", 250.0, 100)
    assert "Product name cannot be empty." in str(exc_info.value)


def test_negative_price_exception():
    with pytest.raises(ValueError):
        Product("Laptop", -250.0, 100)


def test_negative_quantity_exception():
    with pytest.raises(ValueError):
        Product("Laptop", 250.0, -100)


def test_quantity_zero_turn_inactive():
    product = Product("Laptop", 250.0, 100)
    product.set_quantity(0)
    assert product.is_active() is False


def test_buy_reduces_quantity():
    product = Product("Laptop", 250.0, 100)
    product.buy(4)
    assert product.get_quantity() == 96


def test_buy_more_than_quantity_exception():
    product = Product("Laptop", 250.0, 100)
    with pytest.raises(InventoryError):
        product.buy(101)

