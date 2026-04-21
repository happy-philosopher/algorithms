# Напишите класс Queue, который реализует основные операции очереди: enqueue (добавление элемента), dequeue (удаление
# элемента), is_empty (проверка, пуста ли очередь) и peek (просмотр первого элемента в очереди).


class Queue:
    """Класс, реализующий очередь на основе списка."""

    def __init__(self):
        """Инициализирует пустую очередь."""
        self.items = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """
        Удаляет и возвращает первый элемент очереди. Если очередь пуста, вызывает исключение IndexError.
        """
        if self.is_empty():
            raise IndexError("Нельзя удалить элемент из пустой очереди!")
        return self.items.pop(0)

    def is_empty(self):
        """Возвращает True, если очередь пуста, иначе False."""
        return len(self.items) == 0

    def peek(self):
        """
        Возвращает первый элемент очереди без удаления. Если очередь пуста, вызывает исключение IndexError.
        """
        if self.is_empty():
            raise IndexError("Нельзя посмотреть элемент пустой очереди!")
        return self.items[0]


# Пример:
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.peek())        # 10
print(q.dequeue())     # 10
print(q.is_empty())    # False
print(q.dequeue())     # 20
print(q.dequeue())     # 30
print(q.is_empty())    # True
