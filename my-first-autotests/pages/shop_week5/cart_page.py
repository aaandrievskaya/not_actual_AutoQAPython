from playwright.sync_api import expect
from .base_page import BasePage


class CartPage(BasePage):
    """Страница корзины /view_cart"""

    def is_product_in_cart(self, product_name: str) -> bool:
        """Проверяет, что товар с указанным названием присутствует в корзине."""
        # Ищем строку таблицы корзины, содержащую название товара
        product_row = self.page.get_by_text(product_name, exact=False)
        expect(product_row.first).to_be_visible()
        return True
