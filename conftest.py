import pytest
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Browser, sync_playwright


def _get_available_browser(playwright):
    """Выбирает первый доступный браузер"""
    browsers_to_try = [
        ("chromium", playwright.chromium),
        ("firefox", playwright.firefox),
        ("webkit", playwright.webkit)
    ]
    
    for browser_name, browser_type in browsers_to_try:
        try:
            browser = browser_type.launch(headless=True)
            browser.close()
            return browser_name, browser_type
        except Exception:
            continue
    
    raise RuntimeError("Ни один браузер не доступен!")


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser_name, browser_type = _get_available_browser(p)
        print(f"\n=== Запуск тестов в браузере: {browser_name} ===")
        
        browser = browser_type.launch(
            headless=True,
            args=["--disable-dev-shm-usage"]
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


# Allure хук для скриншотов при падении (опционально)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Делает скриншот при падении теста"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot_on_failure",
                attachment_type=AttachmentType.PNG
            )
