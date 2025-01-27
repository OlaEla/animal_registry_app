import sys
import os

# Добавляем каталог `src` в путь поиска модулей
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# from controller.menu_controller import main_menu
from src.controller.menu_controller import main_menu

if __name__ == "__main__":
    main_menu()
