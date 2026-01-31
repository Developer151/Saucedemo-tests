import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
import os

def pytest_addoption(parser):
    """Добавляем возможность передавать браузер через командную строку."""
    parser.addoption("--browser", action="store", default="chromium", 
                     choices=["chromium", "firefox", "webkit"],
                     help="Браузер для запуска тестов: chromium, firefox, webkit")

@pytest.fixture(scope="session")
def browser(request) -> Browser:
    """Фикстура запускает выбранный браузер."""
    browser_name = request.config.getoption("--browser")
    
    with sync_playwright() as p:
        # Выбираем нужный браузер
        if browser_name == "firefox":
            browser = p.firefox.launch(headless=True)  # headless=True — без окна
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)
        else:
            browser = p.chromium.launch(headless=True)  # chromium по умолчанию
        
        yield browser
        browser.close()

# Остальные фикстуры (context, page) остаются как были