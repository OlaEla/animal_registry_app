class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise Exception("Нельзя использовать счетчик после закрытия.")
        self.count += 1

    def close(self):
        self.closed = True
        print(f"Счетчик закрыт. Количество заведенных животных: {self.count}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
