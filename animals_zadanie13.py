# 13.	Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

from datetime import datetime

# Класс для команд
class Command:
    def __init__(self, command_name, description):
        self.command_name = command_name
        self.description = description


# Родительский класс
class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.__birth_date = birth_date  # Приватное поле
        self.commands = []  # Список команд, которые может выполнять животное

    def __calculate_age(self):  # Приватный метод
        today = datetime.today()
        birth_date = datetime.strptime(self.__birth_date, "%Y-%m-%d")
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        if age_months < 0:
            age_years -= 1
            age_months += 12
        return age_years, age_months

    def get_age(self):
        return self.__calculate_age()

    def add_command(self, command):
        """Привязать команду к животному."""
        if isinstance(command, Command):
            self.commands.append(command)
            print(f"Команда '{command.command_name}' добавлена для {self.name}")
        else:
            print("Ошибка: передан неверный объект команды.")

    def perform_command(self, command_name):
        """Выполнить команду, если она доступна животному."""
        for command in self.commands:
            if command.command_name == command_name:
                print(f"{self.name} выполняет команду: {command_name}")
                return
        print(f"{self.name} не знает команду: {command_name}")

    def get_info(self):
        """Вывод информации о животном."""
        age_years, age_months = self.get_age()
        print(f"Имя: {self.name}, Возраст: {age_years} лет и {age_months} месяцев")


# Дочерний класс: Домашние животные
class Pet(Animal):
    def __init__(self, name, birth_date, owner_name):
        super().__init__(name, birth_date)
        self.owner_name = owner_name

    def get_info(self):
        """Вывод информации о домашнем животном."""
        super().get_info()
        print(f"Владелец: {self.owner_name}")


# Дочерний класс: Вьючные животные
class PackAnimal(Animal):
    def __init__(self, name, birth_date, load_capacity):
        super().__init__(name, birth_date)
        self.__load_capacity = load_capacity  # Приватное поле

    def carry_load(self, weight):
        if weight <= self.__load_capacity:
            print(f"{self.name} несет {weight} кг груза.")
        else:
            print(f"{self.name} не может нести {weight} кг. Максимум {self.__load_capacity} кг.")


# Домашние животные
class Dog(Pet):
    def bark(self):
        print(f"{self.name} лает!")


class Cat(Pet):
    def meow(self):
        print(f"{self.name} мяукает!")


class Hamster(Pet):
    def squeak(self):
        print(f"{self.name} пищит!")


# Вьючные животные
class Horse(PackAnimal):
    def neigh(self):
        print(f"{self.name} ржет!")


class Donkey(PackAnimal):
    def bray(self):
        print(f"{self.name} издает характерные звуки!")


class Camel(PackAnimal):
    def grunt(self):
        print(f"{self.name} издает низкие звуки!")


# Тестирование
if __name__ == "__main__":
    # Создаем команды
    sit_command = Command("Сидеть", "Животное садится.")
    jump_command = Command("Прыгать", "Животное прыгает.")

    # Создаем собаку
    buddy = Dog("Бадди", "2020-05-15", "Олег")
    buddy.get_info()  # Информация о животном
    buddy.add_command(sit_command)
    buddy.add_command(jump_command)
    buddy.perform_command("Сидеть")
    buddy.perform_command("Лежать")  # Команда отсутствует
    buddy.bark()  # Проверка уникального метода

    print("\n" + "-" * 50 + "\n")

    # Создаем лошадь
    thunder = Horse("Тандер", "2018-04-19", 150)
    thunder.get_info()  # Информация о лошади
    thunder.add_command(jump_command)
    thunder.perform_command("Прыгать")
    thunder.perform_command("Сидеть")  # Команда отсутствует
    thunder.carry_load(100)  # Лошадь несет 100 кг
    thunder.carry_load(200)  # Превышение допустимого веса
    thunder.neigh()  # Проверка уникального метода

    print("\n" + "-" * 50 + "\n")

    # Создаем кота
    whiskers = Cat("Вискерс", "2021-03-11", "Мария")
    whiskers.get_info()
    whiskers.meow()  # Проверка уникального метода

    print("\n" + "-" * 50 + "\n")

    # Создаем верблюда
    clyde = Camel("Клайд", "2017-08-30", 200)
    clyde.get_info()  # Информация о верблюде
    clyde.carry_load(150)  # Несет груз
    clyde.carry_load(250)  # Превышение допустимого веса
    clyde.grunt()  # Проверка уникального метода
