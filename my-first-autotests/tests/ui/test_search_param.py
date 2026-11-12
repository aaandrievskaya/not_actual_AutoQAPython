import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("query", ["qa", "aqa", "python"])
@pytest.mark.ui
def test_duckduckgo_search_parametrized(page: Page, query: str) -> None:
    page.goto("https://duckduckgo.com/")

    # Устойчивый локатор поисковой строки
    search_input = page.get_by_role("combobox")
    # Печатаем по одной букве, как человек:
    search_input.press_sequentially(query, delay=100)
    # page.locator("button[type='submit']").last.click()
    # page.locator("#react-aria8879024709-_r_3e_").click()
    search_input.press("Enter")

    # Явное ожидание появления результатов
    results = page.locator("article[data-testid='result']")
    expect(results.first).to_be_visible(timeout=10000)

    # Проверка количества результатов
    expect(
        results.nth(9)
    ).to_be_visible()  # пятый есть = не меньше пяти, не «ровно пять»
