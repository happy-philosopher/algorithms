# Реализуйте алгоритм сортировки пузырьком на языке Python.
# Функция должна принимать список и возвращать отсортированный список.

def bubble_sort(arr):
    # Создаём копию списка, чтобы не изменять исходный
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # Внешний цикл — количество проходов
    for i in range(n):
        # Флаг для отслеживания перестановок
        swapped = False

        # Внутренний цикл — сравнение соседних элементов
        # На каждом проходе самый большой элемент «всплывает» в конец
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True

        # Если перестановок не было, список уже отсортирован — выходим
        if not swapped:
            break

    return sorted_arr


# Пример использования
if __name__ == "__main__":
    # Тестовый список
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", test_list)

    # Сортируем список
    sorted_list = bubble_sort(test_list)
    print("Отсортированный список:", sorted_list)
