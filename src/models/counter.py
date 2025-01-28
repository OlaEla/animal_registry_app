import os
import json

class Counter:
    def __init__(self, file_path):
        """
        Инициализирует счётчик, связанный с файлом.
        :param file_path: Путь к файлу counter.json.
        """
        self.file_path = file_path
        self.counter = 0
        self.is_closed = False
        self.is_initialized = False  # Флаг проверки использования блока try-with-resources

        # Загрузка текущего значения из файла, если файл существует
        if os.path.exists(self.file_path):
            self.load_counter()
        else:
            self.save_counter()

    def load_counter(self):
        """Загружает текущее значение счётчика из файла."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.counter = data.get("counter", 0)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Ошибка: не удалось загрузить счётчик. Сбрасываем в 0.")
            self.counter = 0
            self.save_counter()

    def save_counter(self):
        """Сохраняет текущее значение счётчика в файл."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump({"counter": self.counter}, file, ensure_ascii=False, indent=4)

    def add(self):
        """Увеличивает счётчик на 1."""
        if not self.is_initialized:
            raise RuntimeError("Ошибка: метод add() может быть вызван только в блоке try-with-resources.")
        if self.is_closed:
            raise RuntimeError("Ошибка: ресурс уже закрыт. Используйте новый экземпляр Counter.")
        self.counter += 1
        self.save_counter()

    def close(self):
        """Закрывает ресурс."""
        if not self.is_initialized:
            raise RuntimeError("Ошибка: ресурс не был корректно инициализирован.")
        self.is_closed = True

    def __enter__(self):
        """Инициализация ресурса в блоке try-with-resources."""
        self.is_initialized = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Закрытие ресурса в конце блока try-with-resources."""
        self.close()
        self.save_counter()
