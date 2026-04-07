# Создайте отсортированный список из 100 случайных чисел и
# выполните бинарный поиск для нескольких различных значений.
# Запишите результаты.


import random

def binary_search(arr, target):
    """
    Бинарный поиск в отсортированном массиве.
    Возвращает индекс элемента, если найден, иначе -1.
    """
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, iterations
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, iterations


# Шаг 1: Создаём и сортируем список из 100 случайных чисел (от 1 до 500)
random_numbers = [random.randint(1, 1000) for _ in range(100)]
sorted_numbers = sorted(random_numbers)
print("Отсортированный список из 100 случайных чисел:")
print(sorted_numbers)
print("\n" + "="*50 + "\n")

# Шаг 2: Выполняем бинарный поиск для нескольких значений
search_values = [45, 225, 350, sorted_numbers[0], sorted_numbers[-1]]
print("Результаты бинарного поиска:")
print("-" * 50)

for value in search_values:
    index, iterations = binary_search(sorted_numbers, value)
    if index != -1:
        print(f"Значение {value}: найдено на позиции {index} (значение по индексу: {sorted_numbers[index]}), итераций: {iterations}")
    else:
        print(f"Значение {value}: не найдено, выполнено {iterations} итераций")
