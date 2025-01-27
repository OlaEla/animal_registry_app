from datetime import datetime
from typing import List


class Animal:
    # def __init__(self, name: str, birth_date: str):
    #     """
    #     Базовый класс животного.
    #     :param name: Имя животного.
    #     :param birth_date: Дата рождения животного в формате 'YYYY-MM-DD'.
    #     """
    #     self.name = name
    #     self.__birth_date = birth_date
    #     self.commands = []  # Список команд, которые знает животное

    # # def get_age(self):
    # #     """
    # #     Возвращает возраст животного в годах и месяцах.
    # #     :return: Кортеж (лет, месяцев).
    # #     """
    # #     today = datetime.today()
    # #     birth_date = datetime.strptime(self.__birth_date, "%Y-%m-%d")
    # #     years = today.year - birth_date.year
    # #     months = today.month - birth_date.month
    # #     if months < 0:
    # #         years -= 1
    # #         months += 12
    # #     return years, months
    


    # def get_age(self):
    #     today = datetime.today()
    #     birth_date = datetime.strptime(self.__birth_date, "%Y-%m-%d")
    #     age_years = today.year - birth_date.year
    #     age_months = today.month - birth_date.month
    
    # # Корректировка, если текущий месяц раньше месяца рождения
    #     if age_months < 0:
    #         age_years -= 1
    #         age_months += 12
    
    #     return age_years, age_months



    def __init__(self, name: str, birth_date: str):
        """
        Базовый класс животного.
        :param name: Имя животного.
        :param birth_date: Дата рождения животного в формате 'YYYY-MM-DD'.
        """
        self.name = name
        self.birth_date = birth_date
        self.commands = []  # Список команд, которые знает животное

    # def get_age(self):
    #     today = datetime.today()
    #     birth_date = datetime.strptime(self.__birth_date, "%Y-%m-%d")
    #     age_years = today.year - birth_date.year
    #     age_months = today.month - birth_date.month
    
    #     # Корректировка, если текущий месяц раньше месяца рождения
    #     if age_months < 0:
    #         age_years -= 1
    #         age_months += 12
    
    #     return age_years, age_months

    # def __str__(self):
    #     """Возвращает строковое представление возраста животного в формате 'X лет и Y месяцев'."""
    #     years, months = self.get_age()
    #     return f"{years} лет и {months} месяцев"
    


    def get_age(self):
        """ Рассчитать возраст животного.:return: Возраст в годах и месяцах. """
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        today = datetime.today()
        age_in_days = (today - birth_date).days
        years = age_in_days // 365
        months = (age_in_days % 365) // 30
        return years, months

    def __str__(self):
        years, months = self.get_age()
        return f"{years} лет и {months} месяцев"





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

    # def __str__(self):
    #     """
    #     Возвращает строковое представление объекта.
    #     """
    #     years, months = self.get_age()
    #     return f"{self.name}, возраст: {years} лет {months} мес."


class Dog(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
    def sound(self):
        """
        Возвращает звук, который издает собака.
        """
        return f"{self.name} лает!"


class Cat(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
    def sound(self):
        """
        Возвращает звук, который издает кошка.
        """
        return f"{self.name} мяукает!"


class Horse(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
    def sound(self):
        """
        Возвращает звук, который издает лошадь.
        """
        return f"{self.name} ржет!"
    
class Camel(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
    def sound(self):
        return f"{self.name} издает звук верблюда!"

class Donkey(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
    def sound(self):
        return f"{self.name} издает звук осла!"

class Hamster(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
    def sound(self):
        return f"{self.name} пищит!"

