import pytest
from playwright.sync_api import Playwright, sync_playwright


# Список браузеров для параметризации
BROWSERS = ["chromium", "firefox", "webkit"]


@pytest.fixture(scope="function", params=BROWSERS)
def browser_context(request):

    with sync_playwright() as playwright:
        # Получаем тип браузера (chromium, firefox, webkit)
        browser_type = getattr(playwright, request.param)

        # Запускаем браузер
        browser = browser_type.launch(headless=False)  # Будем видеть действия
        context = browser.new_context()  # Создаем новый контекст браузера

        # Передаем контекст браузера в тест
        yield context

        # Закрываем контекст и браузер после теста
        context.close()
        browser.close()
