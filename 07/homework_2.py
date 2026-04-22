# Добавьте в класс HashTable метод resize, который увеличивает размер хеш-таблицы вдвое и
# перераспределяет все элементы. Протестируйте работу метода на примере хеш-таблицы с начальным размером 5,
# добавив в неё 10 элементов.


class HashTable:
    def __init__(self, size=10):
        """Инициализация хеш‑таблицы с заданным размером."""
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0  # Количество элементов в таблице

    def __str__(self):
        """Строковое представление хеш‑таблицы для отладки."""
        result = []
        for i, bucket in enumerate(self.table):
            result.append(f"{i}: {bucket}")
        return "\n".join(result)

    def _hash_function(self, key):
        """Простая хеш‑функция: остаток от деления хеша ключа на размер таблицы."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Вставка пары ключ‑значение в хеш‑таблицу."""
        # Проверяем необходимость увеличения размера (коэффициент загрузки > 0.7)
        if self.count >= self.size * 0.7:
            self.resize()

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
        self.count += 1

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
                self.count -= 1
                return True
        return False

    def resize(self):
        """Увеличивает размер хеш‑таблицы вдвое и перераспределяет все элементы."""
        old_table = self.table
        old_size = self.size

        # Удваиваем размер
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # Перераспределяем все элементы из старой таблицы
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

        print(f"Таблица увеличена до размера {self.size}")

    def get_load_factor(self):
        """Возвращает коэффициент загрузки таблицы (количество элементов / размер)."""
        return self.count / self.size if self.size > 0 else 0


# Тестирование работы метода resize
# Создаём хеш‑таблицу с начальным размером 5
print("Создаём хеш‑таблицу с размером 5")
ht = HashTable(size=5)

print(f"Начальный размер: {ht.size}")
print(f"Коэффициент загрузки: {ht.get_load_factor():.2f}")

# Добавляем 10 элементов
print("\nДобавляем 10 элементов:")
fruits = ["apple", "banana", "cherry", "date", "elderberry",
          "fig", "grape", "honeydew", "kiwi", "lemon"]

for i, fruit in enumerate(fruits):
    ht.insert(fruit, i * 10)
    print(f"Добавлен {fruit}: {i * 10}")

    # Показываем состояние после каждого добавления
    if i in [4, 9]:  # После 5-го и 10-го элемента
        print(f"\nСостояние таблицы после добавления {i + 1} элементов:")
        print(f"Размер: {ht.size}, Количество элементов: {ht.count}")
        print(f"Коэффициент загрузки: {ht.get_load_factor():.2f}")
        print("Содержимое таблицы:")
        print(ht)
        print("-" * 50)

        # Тестируем поиск после перераспределения
        print("\nТестирование поиска после перераспределения:")
        for fruit in ["apple", "grape", "orange"]:
            value = ht.search(fruit)
        if value is not None:
            print(f"Найден {fruit}: {value}")
        else:
            print(f"{fruit} не найден")

        # Тестируем удаление
        print("\nУдаляем 'banana':")
        print(f"Результат удаления: {ht.delete('banana')}")

        print("\nСостояние таблицы после удаления:")
        print(f"Размер: {ht.size}, Количество элементов: {ht.count}")
        print(f"Коэффициент загрузки: {ht.get_load_factor():.2f}")
        print("Содержимое таблицы:")
        print(ht)
