# Реализуйте алгоритм сортировки выбором на языке Python.
# Функция должна принимать список и возвращать отсортированный список.

def selection_sort(arr):
    # Создаём копию списка, чтобы не изменять исходный
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # Проходим по всем элементам списка
    for i in range(n):
        # Предполагаем, что текущий элемент — минимальный
        min_index = i

        # Ищем минимальный элемент в оставшейся неотсортированной части
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j

        # Меняем местами найденный минимальный элемент с первым элементом неотсортированной части
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]

    return sorted_arr


# Пример использования
if __name__ == "__main__":
    # Тестовый список
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", test_list)

    # Сортируем список
    sorted_list = selection_sort(test_list)
    print("Отсортированный список:", sorted_list)
