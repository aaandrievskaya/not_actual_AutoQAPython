import pytest
from playwright.sync_api import Page


@pytest.mark.ui
def test_feautures_items_subset(page: Page) -> None:
    page.goto("https://automationexercise.com/")
    # необходимо принудительно заставить прогрузиться всю страницу перед проверками
    page.wait_for_load_state("networkidle")

    # Находим контейнер секции по заголовку (устойчивый способ)
    page.get_by_text("Features Items").wait_for(state="visible", timeout=10000)
    features_section = page.get_by_text("Features Items").locator("..").locator("..")

    # Собираем все видимые названия товаров внутри секции
    product_names = [
        el.inner_text().strip()
        for el in features_section.locator(".productinfo p").all()
    ]

    # Ключевые товары, которые должны присутствовать (subset)
    expected = {"Blue Top", "Men Tshirt", "Stylish Dress"}

    # Subset-ассерт (главное преимущество)
    assert expected.issubset(
        set(product_names)
    ), f"Не все ожидаемые товары найдены. Найдено: {product_names}"
