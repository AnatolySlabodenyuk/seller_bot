#!/usr/bin/env python3
"""
Setup script for the Telegram curtain calculator bot
"""

import os


def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    if not os.path.exists(env_file):
        print("📝 Создание файла .env...")
        with open(env_file, "w", encoding="utf-8") as f:
            f.write("BOT_TOKEN=your_bot_token_here\n")
        print("✅ Файл .env создан")
        print("⚠️  Не забудьте заменить 'your_bot_token_here' на реальный токен бота!")
    else:
        print("✅ Файл .env уже существует")


def check_dependencies():
    """Check if required packages are installed"""
    required_packages = {
        "aiogram": "aiogram",
        "python-dotenv": "dotenv"
    }
    missing_packages = []

    for pip_name, import_name in required_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(pip_name)

    if missing_packages:
        print(f"❌ Отсутствуют зависимости: {', '.join(missing_packages)}")
        print("Установите их командой: pip install -r requirements.txt")
        return False
    else:
        print("✅ Все зависимости установлены")
        return True


def main():
    """Main setup function"""
    print("🧾 Настройка Telegram-бота для расчёта стоимости штор")
    print("=" * 50)

    # Check dependencies
    if not check_dependencies():
        return

    # Create .env file
    create_env_file()

    print("\n📋 Следующие шаги:")
    print("1. Получите токен бота у @BotFather в Telegram")
    print("2. Отредактируйте файл .env и вставьте токен")
    print("3. Запустите бота: python main.py")

    print("\n🎯 Для тестирования логики расчёта запустите: python test_bot.py")


if __name__ == "__main__":
    main()
