# Автотесты для saucedemo.com

Проект содержит автоматизированные тесты для страницы логина сайта [saucedemo.com](https://www.saucedemo.com/).

## Стек технологий
- Python 3.10
- Playwright
- Pytest
- Allure
- Docker

## Реализованные тест-кейсы

1. ✅ Успешный логин (standard_user / secret_sauce)
2. ✅ Логин с неверным паролем
3. ✅ Логин заблокированного пользователя (locked_out_user)
4. ✅ Логин с пустыми полями
5. ✅ Логин пользователем performance_glitch_user (с учётом возможных задержек)

## Структура проекта
```markdown
## saucedemo_tests/
|-- pages/ # Page Object классы
│   |_login_page.py # Скрипт для работы скрипта по тестам
|-- tests/ # Тесты
│   |_1-5_тесты.py # 5 тестов логина
|-- conftest.py # Фикстуры pytest
|-- Dockerfile # Контейнеризация
|-- .dockerignore #Игнорируемое Dockerом
|-- requirements.txt # Зависимости Python
|-- run-tests.py #Запуск тестов
|-- .gitignore # Игнорируемое Gitом
|__ README.md # Документация
```

## Установка и запуск
### Установка зависимостей
```bash
pip install -r requirements.txt
playwright install chromium   # Установите Chromium для гарантированного запуска
```

**Тесты автоматически выбирают первый доступный браузер в порядке приоритета:**
1. Chromium (рекомендуется)
2. Firefox
3. WebKit (т.е. Safari)

Чтобы запустить все тесты/один тест:
```bash
pytest tests/1-5_тесты.py -v
pytest tests/1-5_тесты.py::TestLogin::test_successful_login -v
```

## Генерация отчетов Allure
### 1. Запустите тесты с сохранением результатов
pytest --alluredir=allure-results
### 2. Сгенерируйте HTML-отчёт
allure generate allure-results -o allure-report --clean
### 3. Откройте отчёт
allure open allure-report

**Примечание: Для работы этих команд требуется установка Allure CLI отдельно. 
А так, run-tests.py всю отчетность автоматом делает.**

### Запуск в Docker
1. Убедитесь, что установлен Docker Desktop
2. Соберите образ и запустите тесты:
```bash
docker build -t saucedemo-tests
docker run --rm saucedemo-tests
```
