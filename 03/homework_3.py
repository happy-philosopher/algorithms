# Сравнение алгоритмов: Сравните время выполнения двух алгоритмов сортировки (пузырьком, выбором и вставками) на
# одинаковых списках. Постройте график зависимости времени выполнения от размера списка для каждого алгоритма.

import time
import random
import matplotlib.pyplot as plt


def bubble_sort(arr):
    """Сортировка пузырьком"""
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr


def selection_sort(arr):
    """Сортировка выбором"""
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
    return sorted_arr


def insertion_sort(arr):
    """Сортировка вставками"""
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


def measure_time(sort_func, data):
    """Измерение времени выполнения"""
    start_time = time.perf_counter()
    sort_func(data)
    end_time = time.perf_counter()
    return end_time - start_time


def test_sorting_algorithm(algorithm_func, algorithm_name, sizes, test_data, completed_tests, total_tests):
    """
    Выполняет тестирование алгоритма сортировки на списках разных размеров и выводит прогресс.

    Параметры:
    algorithm_func: функция алгоритма сортировки,
    algorithm_name: название алгоритма для вывода в консоль,
    sizes: список размеров тестируемых списков,
    test_data: словарь с тестовыми данными по размерам,
    completed_tests: текущее количество выполненных тестов,
    total_tests: общее количество тестов.

    Возвращает:
    tuple: (список времён выполнения, обновлённое количество выполненных тестов)
    """
    times = []
    print(f"\nТестирование {algorithm_name}...")

    for size in sizes:
        test_list = test_data[size]
        test_time = measure_time(algorithm_func, test_list)
        times.append(test_time)
        completed_tests += 1
        progress = (completed_tests / total_tests) * 100
        print(f"{completed_tests} тест из {total_tests}, прогресс: {progress:.1f}% — размер {size}: {test_time:.4f} сек")

    return times, completed_tests


def main():
    # Размеры списков для тестирования
    sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

    # Списки для хранения времени выполнения
    bubble_times = []
    selection_times = []
    insertion_times = []

    # Общее количество тестов для расчёта прогресса
    total_tests = len(sizes) * 3  # 3 алгоритма на каждый размер
    completed_tests = 0

    print("Начинаем тестирование алгоритмов сортировки...")
    print(f"Всего будет выполнено {total_tests} тестов.")

    # Словарь для хранения тестовых списков по размерам
    test_data = {}

    # Создаём тестовые данные для каждого размера — они будут одинаковыми для всех алгоритмов
    for size in sizes:
        test_data[size] = [random.randint(1, 1000) for _ in range(size)]

    # Тестируем все три алгоритма с помощью единой функции
    bubble_times, completed_tests = test_sorting_algorithm(
        bubble_sort, '"СОРТИРОВКА ПУЗЫРЬКОМ"', sizes, test_data, completed_tests, total_tests
    )
    selection_times, completed_tests = test_sorting_algorithm(
        selection_sort, '"СОРТИРОВКА ВЫБОРОМ"', sizes, test_data, completed_tests, total_tests
    )
    insertion_times, completed_tests = test_sorting_algorithm(
        insertion_sort, '"СОРТИРОВКА ВСТАВКАМИ"', sizes, test_data, completed_tests, total_tests
    )

    print(f"\nТестирование завершено! Выполнено {completed_tests} тестов.")
    print("Строим график...")

    # Построение графика
    plt.figure(figsize=(12, 8))
    plt.plot(sizes, bubble_times, 'ro-', label='Сортировка пузырьком', linewidth=2, markersize=8)
    plt.plot(sizes, selection_times, 'bs-', label='Сортировка выбором', linewidth=2, markersize=8)
    plt.plot(sizes, insertion_times, 'g^-', label='Сортировка вставками', linewidth=2, markersize=8)
    plt.xlabel('Размер списка', fontsize=12)
    plt.ylabel('Время выполнения (секунды)', fontsize=12)
    plt.title('Сравнение времени выполнения алгоритмов сортировки', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    # plt.yscale('log')  # Логарифмическая шкала

    # Добавляем аннотации со значениями времени
    for i, size in enumerate(sizes):
        plt.annotate(f'{bubble_times[i]:.4f}', (size, bubble_times[i]), textcoords="offset points",
                     xytext=(0, 10), ha='center', fontsize=8)
        plt.annotate(f'{selection_times[i]:.4f}', (size, selection_times[i]), textcoords="offset points",
             xytext=(0, 10), ha='center', fontsize=8)
        plt.annotate(f'{insertion_times[i]:.4f}', (size, insertion_times[i]), textcoords="offset points",
             xytext=(0, 10), ha='center', fontsize=8)

    plt.tight_layout()
    plt.show()

    print("График построен! Анализ завершён.")


if __name__ == "__main__":
    main()
