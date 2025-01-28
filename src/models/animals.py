from datetime import datetime
from typing import List


class Animal:
    def __init__(self, name: str, birth_date: str, animal_id: int = None):
        """
        Базовый класс животного.
        :param name: Имя животного.
        :param birth_date: Дата рождения животного в формате 'YYYY-MM-DD'.
        :param animal_id: Уникальный идентификатор животного.
        """
        self.id = animal_id  # Поле ID (уникальный идентификатор)
        self.name = name
        self.birth_date = birth_date
        self.commands = []  # Список команд, которые знает животное

    def get_age(self):
        """Рассчитать возраст животного.
        :return: Возраст в годах и месяцах.
        """
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        today = datetime.today()
        age_in_days = (today - birth_date).days
        years = age_in_days // 365
        months = (age_in_days % 365) // 30
        return years, months

    def __str__(self):
        years, months = self.get_age()
        return f"ID: {self.id}, Имя: {self.name}, Возраст: {years} лет и {months} месяцев"

    def add_command(self, command):
        """
        Добавляет новую команду для животного.
        :param command: Объект команды.
        """
        self.commands.append(command)

    def get_commands(self) -> List[str]:
        """
        Возвращает список команд, которые знает животное.
        :return: Список строк (названия команд).
        """
        return [command.command_name for command in self.commands]


# Классы для конкретных животных (Dog, Cat, Horse и т.д.)
class Dog(Animal):
    def __init__(self, name, birth_date, animal_id=None):
        super().__init__(name, birth_date, animal_id)
        self.type = "Dog"

    def sound(self):
        """Возвращает звук, который издаёт собака."""
        return f"{self.name} лает!"


class Cat(Animal):
    def __init__(self, name, birth_date, animal_id=None):
        super().__init__(name, birth_date, animal_id)
        self.type = "Cat"

    def sound(self):
        """Возвращает звук, который издаёт кошка."""
        return f"{self.name} мяукает!"


class Horse(Animal):
    def __init__(self, name, birth_date, animal_id=None):
        super().__init__(name, birth_date, animal_id)
        self.type = "Horse"

    def sound(self):
        """Возвращает звук, который издаёт лошадь."""
        return f"{self.name} ржёт!"


class Camel(Animal):
    def __init__(self, name, birth_date, animal_id=None):
        super().__init__(name, birth_date, animal_id)
        self.type = "Camel"

    def sound(self):
        return f"{self.name} издаёт звук верблюда!"


class Donkey(Animal):
    def __init__(self, name, birth_date, animal_id=None):
        super().__init__(name, birth_date, animal_id)
        self.type = "Donkey"

    def sound(self):
        return f"{self.name} издаёт звук осла!"


class Hamster(Animal):
    def __init__(self, name, birth_date, animal_id=None):
        super().__init__(name, birth_date, animal_id)
        self.type = "Hamster"

    def sound(self):
        return f"{self.name} пищит!"
