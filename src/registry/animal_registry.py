import json
import os
from datetime import datetime
from models.commands import Command
from models.animals import Dog, Cat, Horse, Camel, Donkey, Hamster
from src.models.counter import Counter


class AnimalRegistry:
    def __init__(self, file_path="animals.json"):
        self.file_path = file_path
        self.animals = []


    def load_animals(self):
        """Загружает животных из файла animals.json."""
        try:
            print("Загрузка данных из animals.json...")
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            animals = []
            for animal_data in data:
                animal_type = animal_data["type"].lower()
                if animal_type == "dog":
                    animal = Dog(animal_data["name"], animal_data["birth_date"])
                elif animal_type == "cat":
                    animal = Cat(animal_data["name"], animal_data["birth_date"])
                elif animal_type == "horse":
                    animal = Horse(animal_data["name"], animal_data["birth_date"])
                elif animal_type == "camel":
                    animal = Camel(animal_data["name"], animal_data["birth_date"])
                elif animal_type == "donkey":
                    animal = Donkey(animal_data["name"], animal_data["birth_date"])
                elif animal_type == "hamster":
                    animal = Hamster(animal_data["name"], animal_data["birth_date"])
                else:
                    print(f"Неизвестный тип животного: {animal_type}")
                    continue

                # Присваиваем id животному
                animal.id = animal_data["id"]

                # Загружаем команды, если есть
                if "commands" in animal_data:
                    for command_data in animal_data["commands"]:
                        command = Command(command_data["command_name"], command_data["description"])
                        animal.add_command(command)

                animals.append(animal)

            return animals

        except FileNotFoundError:
            print("Файл animals.json не найден.")
            return []
        except json.JSONDecodeError:
            print("Ошибка при чтении файла animals.json.")
            return []


    def save_animals(self, animals):
        """Сохранить животных в файл JSON."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [
                    {   
                        "id": animal.id,
                        "name": animal.name,
                        "birth_date": animal.birth_date,
                        "type": type(animal).__name__,
                        "commands": [
                            {
                                "command_name": cmd.command_name,
                                "description": cmd.description
                            }
                            for cmd in animal.commands
                        ]
                    }
                    for animal in animals
                ],
                file,
                ensure_ascii=False,
                indent=4
            )


    def add_new_animal(self):
        """Добавить новое животное в реестр."""
        name = input("Введите имя нового животного: ")
        birth_date = input("Введите дату рождения животного (в формате YYYY-MM-DD): ")

        print("Выберите тип животного:")
        print("1. Собака")
        print("2. Кошка")
        print("3. Лошадь")
        print("4. Хомяк")
        print("5. Верблюд")
        print("6. Осел")

        try:
            choice = int(input("Введите номер типа: "))
        except ValueError:
            print("Ошибка: неверный ввод.")
            return

        class_mapping = {
            1: Dog,
            2: Cat,
            3: Horse,
            4: Hamster,
            5: Camel,
            6: Donkey
        }

        if choice not in class_mapping:
            print("Ошибка: указан некорректный тип животного.")
            return

        # Определяем класс животного и создаём объект
        animal_class = class_mapping[choice]
        new_animal = animal_class(name, birth_date)

        # Генерируем уникальный ID для нового животного
        existing_animals = self.load_animals()
        max_id = max([animal.id for animal in existing_animals], default=0)
        new_animal.id = max_id + 1

        # Добавляем новое животное в список
        existing_animals.append(new_animal)

        # Сохраняем обновленный список животных обратно в файл
        self.save_animals(existing_animals)


        # Работа с Counter
        counter_file_path = "counter.json"
        try:
            with Counter(counter_file_path) as counter:
                counter.add()
                print(f"Животное {name} добавлено в реестр с ID {new_animal.id}.")
                print(f"Всего добавлено животных: {counter.counter}.")
        except RuntimeError as e:
            print(f"Ошибка: {e}")

    def get_all_animals(self):
        """Загружает и возвращает список всех животных, одновременно выводя их на экран."""
        if not self.animals:
            self.animals = self.load_animals()
        
        if not self.animals:
            print("Реестр пуст.")
        else:
            print("Список всех животных:")
            for animal in self.animals:
                years, months = animal.get_age()  # Получаем возраст в годах и месяцах
                # print(f"- {animal.name} ({animal.__class__.__name__}), возраст: {years} лет и {months} месяцев")
                print(f"- ID: {animal.id}, {animal.name} ({animal.__class__.__name__}), возраст: {years} лет и {months} месяцев")

                 
        
        return self.animals

    def get_animal_by_name(self, name):
        """Найти животное по имени."""
        if not self.animals:  # Если список животных пуст, загрузите их
            self.animals = self.load_animals()
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None

    def show_animal_commands(self, animal_name):
        """Показать команды, которые знает животное."""
        animal = self.get_animal_by_name(animal_name)
        if animal:
            commands = animal.get_commands()
            if commands:
                return f"Команды для {animal.name}: {', '.join(commands)}"
            else:
                return f"{animal.name} пока не знает команд."
        else:
            return "Животное не найдено."


    def train_animal(self, animal_name, command_name, command_description):
        """Обучить животное новой команде.
    :param animal_name: Имя животного.
    :param command_name: Название команды.
    :param command_description: Описание команды.
    :return: Строка с результатом операции.
    """
        animal = self.get_animal_by_name(animal_name)
        if animal:
            # Проверка на существование команды
            existing_commands = [cmd.command_name for cmd in animal.commands]
            if command_name in existing_commands:
                return f"{animal.name} уже знает команду '{command_name}'."
    
            # Создание новой команды
            command = Command(command_name, command_description)
            animal.add_command(command)

            # print(f"Команды для {animal.name} перед сохранением: {[cmd.command_name for cmd in animal.commands]}")  # Отладка
        
            # Сохраняем обновленный список животных
            self.save_animals(self.animals)  # Сохранить изменения
            return f"{animal.name} успешно обучен команде '{command_name}'."
        else:
            return "Животное не найдено."





    def change_animal_class(self):
        """Изменить класс животного."""
        name = input("Введите имя животного, которое хотите перенести в другой класс: ")
        self.animals = self.load_animals()
        animal = next((a for a in self.animals if a.name == name), None)

        if not animal:
            print("Животное с таким именем не найдено.")
            return

        print(f"Текущее животное: {animal.name} ({animal.__class__.__name__})")
        print("Выберите новый класс:")
        print("1. Dog")
        print("2. Cat")
        print("3. Horse")
        print("4. Hamster")
        print("5. Camel")
        print("6. Donkey")

        try:
            choice = int(input("Введите номер нового класса: "))
        except ValueError:
            print("Неверный ввод. Попробуйте снова.")
            return

        class_mapping = {
            1: Dog,
            2: Cat,
            3: Horse,
            4: Hamster,
            5: Camel,
            6: Donkey
        }

        if choice not in class_mapping:
            print("Неверный выбор. Попробуйте снова.")
            return

        new_class = class_mapping[choice]
        new_animal = new_class(animal.name, animal.birth_date)
        new_animal.id = animal.id

        # Удаляем старое животное и добавляем новое
        self.animals.remove(animal)
        self.animals.append(new_animal)
        self.save_animals(self.animals)

        print("Данные успешно обновлены.")




    
