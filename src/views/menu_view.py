def print_main_menu():
    print("\n--- Реестр животных ---")
    print("1. Завести новое животное")
    print("2. Посмотреть список команд животного")
    print("3. Обучить животное новой команде")
    print("4. Показать всех животных")
    print("5. Выйти")

def get_user_choice():
    return input("Выберите действие: ")

def print_message(message):
    print(message)
