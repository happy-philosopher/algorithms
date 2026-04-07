# Сравните время выполнения бинарного поиска и линейного
# поиска на одинаковых списках. Постройте график зависимости
# времени выполнения от размера списка для обоих алгоритмов.


import time
import random
import matplotlib.pyplot as plt

# Реализация линейного поиска
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Реализация бинарного поиска (работает только с отсортированными списками)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Функция для измерения времени выполнения алгоритма
def measure_time(search_func, arr, target):
    start_time = time.perf_counter()  # Более точный таймер
    search_func(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time

# Основная функция тестирования алгоритмов
def compare_search_algorithms(sizes, num_iterations=100):
    linear_times = []
    binary_times = []

    for size in sizes:
        # Генерация случайного списка и сортировка для бинарного поиска
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)  # Гарантируем, что элемент есть в списке

        # Измеряем время линейного поиска (на отсортированном списке)
        linear_time = sum(measure_time(linear_search, arr, target)
                           for _ in range(num_iterations)) / num_iterations

        # Измеряем время бинарного поиска
        binary_time = sum(measure_time(binary_search, arr, target)
                         for _ in range(num_iterations)) / num_iterations

        linear_times.append(linear_time)
        binary_times.append(binary_time)

    return linear_times, binary_times


# Основные параметры тестирования
sizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Сравниваем алгоритмы
linear_times, binary_times = compare_search_algorithms(sizes)

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label='Линейный поиск', marker='o')
plt.plot(sizes, binary_times, label='Бинарный поиск', marker='s')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение времени выполнения линейного и бинарного поиска')
plt.legend()
plt.grid(True)
plt.show()
