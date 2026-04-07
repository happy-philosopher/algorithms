# Реализуйте алгоритм бинарного поиска на языке Python. Функция
# должна принимать отсортированный список и элемент для поиска,
# и возвращать индекс элемента или -1, если элемент не найден.


def binary_search(sorted_list, target):
    """
    Итеративная реализация бинарного поиска.
    Args:
        sorted_list (list): Отсортированный список для поиска.
        target: Элемент, который нужно найти.
    Returns:
        int: Индекс элемента в списке или -1, если элемент не найден.
    """
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        # Вычисляем индекс среднего элемента
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            # Элемент найден, возвращаем его индекс
            return mid
        elif sorted_list[mid] < target:
            # Искомый элемент находится в правой половине
            left = mid + 1
        else:
            # Искомый элемент находится в левой половине
            right = mid - 1
    # Элемент не найден
    return -1


# Тестовый отсортированный список
test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Проверка работы итеративной версии
print(binary_search(test_list, 7))
print(binary_search(test_list, 4))
print(binary_search(test_list, 1))
print(binary_search(test_list, 19))
print(binary_search([], 5))
