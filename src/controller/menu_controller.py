from src.registry.animal_registry import AnimalRegistry
from views.menu_view import print_message
from models.animals import Dog, Cat, Horse
from models.commands import Command
from models.counter import Counter


# Глобальный экземпляр реестра
animal_registry = AnimalRegistry()

def main_menu():
    while True:
        print("\n--- Реестр животных ---")
        print("1. Завести новое животное")
        print("2. Посмотреть список команд животного")
        print("3. Обучить животное новой команде")
        print("4. Показать всех животных")
        print("5. Определить животное в правильный класс")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            animal_registry.add_new_animal()  # Метод для добавления нового животного
        elif choice == "2":
            show_animal_commands()
        elif choice == "3":
            train_animal()
        elif choice == "4":
            animal_registry.get_all_animals()
        elif choice == "5":
            animal_registry.change_animal_class()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def add_new_animal():
    """Завести новое животное."""
    animal_registry.add_new_animal()



def show_animal_commands():
    """Показать команды, которые знает животное."""
    name = input("Введите имя животного: ")
    result = animal_registry.show_animal_commands(name)
    print(result)

def train_animal():
    """Обучить животное новой команде."""
    name = input("Введите имя животного: ")
    command_name = input("Введите название новой команды: ")
    command_description = input("Введите описание команды: ")
    result = animal_registry.train_animal(name, command_name, command_description)
    print(result)

# Точка входа в программу
if __name__ == "__main__":
    main_menu()