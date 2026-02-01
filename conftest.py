import pytest

# Теперь фикстуры page, context, browser предоставляются плагином pytest-playwright

def pytest_addoption(parser):
    """Опция для выбора браузера"""
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Браузер для тестов: chromium, firefox, webkit"
    )

@pytest.fixture(scope="session")
def browser_type_launch_args(pytestconfig):
    """Выбор браузера через параметр"""
    return {"browser_type": pytestconfig.getoption("--browser")}
