# Используйте написанную хеш-функцию для создания словаря, в котором ключами являются строки,
# а значениями — их хеш-значения. Реализуйте функции добавления элемента в словарь и поиска значения по ключу.


def simple_hash(key, table_size):
    """Простая хеш-функция для строк."""
    hash_value = 0
    for index, char in enumerate(key):
        hash_value += ord(char) * (index + 1)
    return hash_value % table_size


class HashDictionary:
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def add(self, key, value):
        """Добавляет элемент в словарь."""
        index = simple_hash(key, self.size)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1
        if self.count / self.size > 0.7:
            self._resize()

    def get(self, key):
        """Получает значение по ключу."""
        index = simple_hash(key, self.size)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"Ключ '{key}' не найден")

    def _resize(self):
        """Расширяет таблицу при высокой загрузке."""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for chain in old_table:
            for key, value in chain:
                self.add(key, value)


# Пример:
# Создаём словарь
hash_dict = HashDictionary()

# Добавляем элементы
hash_dict.add("apple", 10)
hash_dict.add("banana", 20)
hash_dict.add("cherry", 30)

# Получаем значения
print(hash_dict.get("apple"))   # Вывод: 10
print(hash_dict.get("banana"))  # Вывод: 20
print(hash_dict.get("cherry"))  # Вывод: 30

# Обновляем значение
hash_dict.add("apple", 15)
print(hash_dict.get("apple"))   # Вывод: 15
