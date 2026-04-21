# Напишите функцию для реализации сортировки слиянием (MergeSort) с примером использования.


def merge_sort(arr):
    """
    Сортировка слиянием (Merge Sort).
    Args:
        arr: список элементов для сортировки
    Returns:
        Отсортированный список
    """
    # Базовый случай: если массив содержит 0 или 1 элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем обе половины
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Сливаем отсортированные половины в один массив
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Функция слияния двух отсортированных массивов.
    Args:
        left: отсортированный левый массив
        right: отсортированный правый массив
    Returns:
        Объединённый отсортированный массив
    """
    result = []  # Результирующий массив
    i = j = 0  # Индексы для левого и правого массивов

    # Сравниваем элементы из обоих массивов и добавляем меньший в результат
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левого массива (если есть)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из правого массива (если есть)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Пример 1: сортировка списка чисел
numbers = [38, 27, 43, 3, 9, 82, 10]
print("Исходный массив:", numbers)
sorted_numbers = merge_sort(numbers)
print("Отсортированный массив:", sorted_numbers)

# Пример 2: сортировка списка строк
words = ["banana", "apple", "cherry", "date"]
print("\nИсходный массив строк:", words)
sorted_words = merge_sort(words)
print("Отсортированный массив строк:", sorted_words)

# Пример 3: сортировка с отрицательными числами
mixed_numbers = [-5, 0, 3, -1, 8, -10, 2]
print("\nИсходный массив с отрицательными числами:", mixed_numbers)
sorted_mixed = merge_sort(mixed_numbers)
print("Отсортированный массив:", sorted_mixed)
