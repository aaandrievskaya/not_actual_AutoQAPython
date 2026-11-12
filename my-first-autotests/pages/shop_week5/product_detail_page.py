from playwright.sync_api import expect
from .base_page import BasePage
from .cart_page import CartPage


class ProductDetailPage(BasePage):
    """Страница детальной информации о товаре"""

    def add_to_cart(self) -> CartPage:
        """Добавляет товар, закрывает окно Added! и возвращает корзину."""
        self.page.get_by_role("button", name="Add to cart").click()
        expect(self.page.get_by_text("Added!")).to_be_visible()
        self.page.get_by_role("link", name="View Cart").click()
        self.page.wait_for_load_state("domcontentloaded")
        return CartPage(self.page)

    def product_title(self) -> str:
        """Имя открытого товара — его же потом ищут в корзине."""
        return (
            self.page.locator(".product-information")
            .get_by_role("heading")
            .first.inner_text()
        )

    def go_to_cart(self) -> CartPage:
        """Прямой переход в корзину (если нужно)."""
        self.page.goto("https://automationexercise.com/view_cart")
        return CartPage(self.page)
