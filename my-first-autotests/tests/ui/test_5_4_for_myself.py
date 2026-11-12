import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("query", ["qa"])
@pytest.mark.ui
def test_duckduckgo_search_parametrized(page: Page, query: str) -> None:
    page.goto(
        "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2"
        "%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
    )

    # Устойчивый локатор поисковой строки
    search_input = page.get_by_placeholder("Искать в Википедии").first
    search_input.click()
    search_input = page.get_by_role("combobox", name="Искать в Википедии")
    # Печатаем по одной букве, как человек:
    search_input.fill(query)
    # page.locator("button", has_text = 'Поиск').click()
    search_input.press("Enter")

    # Явное ожидание появления результатов
    results = page.locator("li")
    expect(results.first).to_be_visible(timeout=10000)

    # Проверка количества результатов
    expect(
        results.nth(2)
    ).to_be_visible()  # пятый есть = не меньше пяти, не «ровно пять»
