# Напишите класс Stack, который реализует основные операции стека: push, pop, is_empty и peek.


class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self._items = []

    def push(self, item):
        """
        Добавляет элемент на вершину стека.
        Args:
            item: элемент, который нужно добавить.
        """
        self._items.append(item)

    def pop(self):
        """
        Удаляет и возвращает элемент с вершины стека.
        Returns:
            Элемент с вершины стека.
        Raises:
            IndexError: если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Нельзя взять из пустого стека!")
        return self._items.pop()

    def peek(self):
        """
        Возвращает элемент с вершины стека без его удаления.
        Returns:
            Элемент с вершины стека.
        Raises:
            IndexError: если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Нельзя скопировать из пустого стека!")
        return self._items[-1]

    def is_empty(self):
        """
        Проверяет, пуст ли стек.
        Returns:
            bool: True, если стек пуст, False — в противном случае.
        """
        return len(self._items) == 0

    def size(self):
        """
        Возвращает количество элементов в стеке.
        Returns:
            int: количество элементов в стеке.
        """
        return len(self._items)


# Пример:
# Создаём экземпляр стека
stack = Stack()

# Проверяем, пуст ли стек
print(stack.is_empty())  # True

# Добавляем элементы
stack.push(1)
stack.push(2)
stack.push(3)

# Смотрим верхний элемент
print(stack.peek())  # 3

# Удаляем элементы по одному
print(stack.pop())  # 3
print(stack.pop())  # 2

# Проверяем размер стека
print(stack.size())  # 1

# Ещё раз проверяем, пуст ли стек
print(stack.is_empty())  # False
