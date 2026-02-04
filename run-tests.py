"""
Основной скрипт запуска тестов.
Запускает тесты и генерирует Allure отчёт если установлен Allure CLI.
Если Allure не установлен - выводит инструкцию по установке.
"""

import subprocess
import sys
import os
import shutil


def check_allure():
    """Проверяет, установлен ли Allure CLI"""
    try:
        result = subprocess.run(
            ["allure", "--version"],
            capture_output=True,
            text=True,
            shell=True
        )
        return result.returncode == 0
    except:
        return False


def run_tests():
    """Запускает pytest тесты"""
    print("🚀 Запуск тестов...")
    
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--alluredir=allure-results",
        "--clean-alluredir"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    print("\n" + "="*60)
    print("РЕЗУЛЬТАТЫ ТЕСТОВ:")
    print("="*60)
    print(result.stdout)
    
    if result.stderr:
        print("\nПРЕДУПРЕЖДЕНИЯ/ОШИБКИ:")
        print(result.stderr)
    
    return result.returncode


def generate_allure_report():
    """Генерирует Allure отчёт"""
    if not os.path.exists("allure-results"):
        print("❌ Нет результатов тестов для генерации отчёта")
        return False
    
    print("\n📊 Генерация Allure отчёта...")
    
    try:
        # Удаляем старый отчёт если есть
        if os.path.exists("allure-report"):
            shutil.rmtree("allure-report")
        
        # Генерируем новый отчёт
        result = subprocess.run(
            ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"],
            capture_output=True,
            text=True,
            shell=True
        )
        
        if result.returncode == 0:
            print("✅ Allure отчёт сгенерирован: allure-report/index.html")
            
            # Пытаемся открыть в браузере
            try:
                subprocess.run(["allure", "open", "allure-report"], shell=True)
            except:
                print("📂 Откройте файл вручную: allure-report/index.html")
            
            return True
        else:
            print(f"❌ Ошибка генерации отчёта: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def main():
    print("="*60)
    print("🧪 SAUCEDEMO TESTS - ALLURE REPORT")
    print("="*60)
    
    # Проверяем Allure
    if not check_allure():
        print("\n⚠️  Allure CLI не установлен!")
        print("="*60)
        print("УСТАНОВИТЕ ALLURE CLI ДЛЯ ГЕНЕРАЦИИ ОТЧЁТОВ:")
        print("="*60)
        print("1. Скачайте с https://github.com/allure-framework/allure2/releases")
        print("2. Распакуйте и добавьте bin/ в PATH")
        print("3. Или установите через package manager:")
        print("   • Windows: scoop install allure")
        print("   • Mac: brew install allure")
        print("   • Linux: sudo apt-get install allure")
        print("\nЗапуск тестов без отчёта...")
        print("="*60)
    
    # Запускаем тесты
    exit_code = run_tests()
    
    # Если Allure установлен - генерируем отчёт
    if check_allure():
        generate_allure_report()
    else:
        print("\n📝 Для генерации Allure отчёта установите Allure CLI")
        print("   (см. инструкцию выше)")
    
    print("\n" + "="*60)
    print(f"🎉 ТЕСТЫ ЗАВЕРШЕНЫ. Код возврата: {exit_code}")
    print("="*60)
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
