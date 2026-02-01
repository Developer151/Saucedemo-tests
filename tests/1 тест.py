import allure
import pytest
from pages.login page import LoginPage

@allure.title("Успешный логин стандартным пользователем")
def test_successful_login(page):  # 'page' — это фикстура, которую предоставит Playwright
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Проверяем, что мы перешли на нужную страницу
    assert page.url == "https://www.saucedemo.com/inventory.html"
    # Проверяем, что виден заголовок
    assert page.is_visible(".title")
