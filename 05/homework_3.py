# Напишите функцию для реализации быстрой сортировки
# (QuickSort) с примером использования.


def quicksort(arr):
    """
    Быстрая сортировка (QuickSort) — рекурсивный алгоритм сортировки.
    Args:
        arr (list): Список для сортировки
    Returns:
        list: Отсортированный список
    """
    # Базовый случай: если массив пустой или содержит один элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент (pivot) — в данном случае средний элемент
    pivot = arr[len(arr) // 2]

    # Разделяем массив на три части:
    # - элементы меньше опорного
    left = [x for x in arr if x < pivot]
    # - элементы равные опорному
    middle = [x for x in arr if x == pivot]
    # - элементы больше опорного
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортируем левую и правую части и объединяем результаты
    return quicksort(left) + middle + quicksort(right)


# Пример использования
if __name__ == "__main__":
    # Исходный массив
    unsorted_array = [3, 6, 8, 10, 1, 2, 1, 23, 2, 4, 7, 12, 88, 53]
    print("Исходный массив:", unsorted_array)

    # Сортируем массив
    sorted_array = quicksort(unsorted_array)
    print("Отсортированный массив:", sorted_array)
