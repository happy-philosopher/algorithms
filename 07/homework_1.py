# Напишите класс HashTable, который реализует основные операции хеш-таблицы:
# insert (вставка элемента), search (поиск элемента) и delete (удаление элемента).


class HashTable:
    def __init__(self, size=10):
        """Инициализация хеш‑таблицы с заданным размером."""
        self.size = size
        # Используем список списков для реализации метода цепочек (chaining)
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        """Простая хеш‑функция: остаток от деления хеша ключа на размер таблицы."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставка пары ключ‑значение в хеш‑таблицу."""
        index = self._hash_function(key)
        bucket = self.table[index]

        # Проверяем, существует ли ключ уже в бакете
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Если ключ найден, обновляем значение
                bucket[i] = (key, value)
                return

        # Если ключ не найден, добавляем новую пару
        bucket.append((key, value))

    def search(self, key):
        """Поиск значения по ключу. Возвращает значение или None, если ключ не найден."""
        index = self._hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Удаление пары ключ‑значение по ключу.
        Возвращает True, если элемент был удалён, False — если ключ не найден."""
        index = self._hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        """Строковое представление хеш‑таблицы для отладки."""
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"{i}: {bucket}")
        return "\n".join(result)


# Создаём хеш‑таблицу
ht = HashTable(size=5)

# Вставляем элементы
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)

# Ищем элементы
print(ht.search("apple"))   # Вывод: 10
print(ht.search("grape"))    # Вывод: None

# Удаляем элемент
print(ht.delete("banana")) # Вывод: True
print(ht.delete("kiwi"))   # Вывод: False

# Выводим содержимое таблицы
print(ht)
