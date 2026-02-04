import allure
import pytest
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from pages.login_page import LoginPage


@allure.epic("SauceDemo")
@allure.feature("Авторизация")
class TestLogin:
    """Тесты для страницы логина"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Фикстура: создание Page Object перед каждым тестом"""
        self.login_page = LoginPage(page)
        self.login_page.navigate()
        self.login_page.should_have_login_elements()
    
    @allure.title("Успешный логин стандартным пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Позитивные сценарии")
    def test_successful_login(self):
        """1. Успешный логин (standard_user / secret_sauce)"""
        with allure.step("Ввести корректные логин и пароль"):
            self.login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Проверить переход на главную страницу"):
            self.login_page.should_be_on_inventory_page()
    
    @allure.title("Логин с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Негативные сценарии")
    def test_login_with_wrong_password(self):
        """2. Логин с неверным паролем"""
        self.login_page.login("standard_user", "wrong_password")
        self.login_page.should_show_error("Username and password do not match")
    
    @allure.title("Логин заблокированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Негативные сценарии")
    def test_login_locked_out_user(self):
        """3. Логин заблокированного пользователя (locked_out_user)"""
        self.login_page.login("locked_out_user", "secret_sauce")
        self.login_page.should_show_error("Sorry, this user has been locked out")
    
    @allure.title("Логин с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Валидация полей")
    def test_login_empty_fields(self):
        """4. Логин с пустыми полями"""
        self.login_page.click_login()
        self.login_page.should_show_error("Username is required")
    
    @allure.title("Логин пользователем performance_glitch_user")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Сценарии с задержками")
    def test_login_performance_glitch_user(self):
        """5. Логин пользователем performance_glitch_user"""
        self.login_page.page.set_default_timeout(10000)
        self.login_page.login("performance_glitch_user", "secret_sauce")
        self.login_page.should_be_on_inventory_page()
