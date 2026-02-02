import pytest
from playwright.sync_api import Browser, sync_playwright
import sys

def _get_available_browser(playwright):
    """Выбирает первый доступный браузер в порядке приоритета"""
    browsers_to_try = [
        ("chromium", playwright.chromium),
        ("firefox", playwright.firefox),
        ("webkit", playwright.webkit)
    ]
    
    for browser_name, browser_type in browsers_to_try:
        try:
            # Пробуем запустить браузер
            browser = browser_type.launch(headless=True)
            browser.close()
            return browser_name, browser_type
        except Exception:
            # Этот браузер не установлен или не работает
            continue
    
    # Если ни один не сработал
    raise RuntimeError(
        "Ни один браузер не доступен! Установите: "
        "playwright install chromium  # или firefox, webkit"
    )


@pytest.fixture(scope="session")
def browser() -> Browser:
    """Запускает первый доступный браузер"""
    with sync_playwright() as p:
        browser_name, browser_type = _get_available_browser(p)
        print(f"\n=== Запуск тестов в браузере: {browser_name} ===")
        
        browser = browser_type.launch(
            headless=True,  # False для отладки с окном
            args=["--disable-dev-shm-usage"]  # важно для Docker
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    """Новый контекст для каждого теста"""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Новая вкладка для каждого теста"""
    page = context.new_page()
    yield page
    page.close()
