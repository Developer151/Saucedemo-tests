# Автотесты для saucedemo.com

Проект содержит автоматизированные тесты для страницы логина сайта [saucedemo.com](https://www.saucedemo.com/).

## Стек технологий
- Python 3.10
- Playwright
- Pytest
- Allure
- Docker

## Структура проекта
(потом составлю)

## Установка и запуск
### Запуск тестов

Тесты автоматически выбирают первый доступный браузер в порядке приоритета:
1. Chromium (рекомендуется)
2. Firefox (если нет Chrome)
3. WebKit (т.е. Safari)
# Запуск в Docker

1. Убедитесь, что установлен Docker Desktop
2. Соберите образ:
```bash
docker build -t saucedemo-tests .

**Для гарантированного запуска установите Chromium:**
```bash
playwright install chromium
