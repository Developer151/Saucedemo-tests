# Используем официальный образ Playwright с Python 3.10 (как в ТЗ)
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры Playwright (уже есть в образе, но на всякий случай)
RUN playwright install chromium
RUN playwright install firefox

# Копируем весь проект
COPY . .

# Команда по умолчанию - запуск тестов
CMD ["pytest", "tests/", "-v", "--alluredir=allure-results"]
