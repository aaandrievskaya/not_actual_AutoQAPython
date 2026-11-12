import pytest
from playwright.sync_api import Page
from pages.shop_week5.home_page import HomePage


@pytest.mark.ui
def test_add_product_to_cart_and_verify(page: Page) -> None:
    home = HomePage(page)
    home.goto("https://automationexercise.com/")
    products = home.go_to_products()
    detail = products.open_first_product()
    product_name = detail.product_title()
    product_name = detail.product_title()
    print(f"\n---> ВОТ ЧТО ЛЕЖИТ В ПЕРЕМЕННОЙ: '{product_name}' <---")
    cart = detail.add_to_cart()
    assert cart.is_product_in_cart(product_name) is True
