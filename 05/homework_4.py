# Проанализируйте время выполнения быстрой сортировки на списках различной длины
# (например, 10, 100, 1000 элементов) и сравните её с другими сортировками, такими как сортировка вставками.


import time
import random
import matplotlib.pyplot as plt
import tracemalloc


def quicksort(arr):
    """
    Быстрая сортировка (Quicksort) — алгоритм «разделяй и властвуй».
    Выбирает опорный элемент, разделяет массив на части и рекурсивно сортирует их.
    Средняя сложность: O(n log n), худшая: O(n²).
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def insertion_sort(arr):
    """
    Сортировка вставками (Insertion Sort) — последовательно вставляет каждый элемент
    в правильное место в уже отсортированной части массива.
    Сложность: O(n²) в среднем и худшем случае, O(n) в лучшем (если массив уже отсортирован).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """
    Сортировка слиянием (Merge Sort) — рекурсивно делит массив пополам, затем сливает отсортированные части.
    Гарантированная сложность O(n log n) во всех случаях.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """
    Вспомогательная функция для merge_sort: сливает два отсортированных массива в один.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heapify(arr, n, i):
    """
    Вспомогательная функция для heap_sort: восстанавливает свойство кучи для поддерева с корнем i.
    n — размер кучи.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Пирамидальная сортировка (Heap Sort) — строит двоичную кучу, затем извлекает элементы по одному.
    Сложность O(n log n) во всех случаях, сортирует на месте.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def generate_test_cases(sizes):
    """
    Генерирует тестовые массивы для заданных размеров: случайные, отсортированные и в обратном порядке.
    Возвращает словарь: {размер: {тип_данных: массив}}.
    """
    test_cases = {}
    for size in sizes:
        random_arr = [random.randint(1, 1000) for _ in range(size)]
        sorted_arr = sorted(random_arr)
        reverse_arr = sorted_arr[::-1]
        test_cases[size] = {
            'random': random_arr,
            'sorted': sorted_arr,
            'reverse': reverse_arr
        }
    return test_cases


def measure_time_and_memory(sort_func, arr):
    """
    Измеряет время выполнения и пиковое потребление памяти для функции сортировки.
    Использует time.perf_counter() для времени и tracemalloc для памяти.
    Возвращает: (время в секундах, пиковая память в байтах).
    """
    tracemalloc.start()
    start_time = time.perf_counter()
    sorted_arr = sort_func(arr.copy())
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak


def run_experiment(sizes, num_runs=10):
    """
    Запускает серию тестов для всех алгоритмов на всех тестовых массивах.
    Выполняет num_runs запусков для усреднения результатов.
    Возвращает вложенный словарь с результатами: {размер: {тип: {алгоритм: {время, память}}}}.
    """
    test_cases = generate_test_cases(sizes)
    results = {}

    algorithms = {
        'quicksort': quicksort,
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'heap_sort': heap_sort
    }

    for size in sizes:
        results[size] = {}
        for case_type, arr in test_cases[size].items():
            results[size][case_type] = {}
            for name, func in algorithms.items():
                times = []
                memories = []
                for _ in range(num_runs):
                    time_taken, memory_used = measure_time_and_memory(func, arr)
                    times.append(time_taken)
                    memories.append(memory_used)
                avg_time = sum(times) / len(times)
                avg_memory = sum(memories) / len(memories)
                results[size][case_type][name] = {
                    'time': avg_time,
                    'memory': avg_memory
                }
    return results


def plot_results(results, sizes):
    """
    Строит графики времени выполнения для каждого типа данных (случайные, отсортированные, обратные).
    На каждом графике отображаются линии для всех четырёх алгоритмов.
    Использует matplotlib для визуализации.
    """
    # Создаём 3 графика (по одному на каждый тип данных)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15), constrained_layout=True)
    axes = [ax1, ax2, ax3]
    case_types = ['random', 'sorted', 'reverse']
    algorithms = ['quicksort', 'insertion_sort', 'merge_sort', 'heap_sort']
    colors = ['blue', 'red', 'green', 'orange']

    for case_idx, case_type in enumerate(case_types):
        ax = axes[case_idx]
        ax.set_title(f'Время выполнения — {case_type} данные')
        ax.set_xlabel('Размер массива')
        ax.set_ylabel('Среднее время (секунды)')

        for alg_idx, alg_name in enumerate(algorithms):
            times = [results[size][case_type][alg_name]['time'] for size in sizes]
            ax.plot(sizes, times, marker='o', color=colors[alg_idx], label=alg_name)

        ax.legend()
        ax.grid(True)
        ax.set_yscale('log')  # Логарифмическая шкала для оси Y на каждом графике

    plt.show()



def print_detailed_results(results, sizes):
    """
    Выводит подробные результаты в табличном формате: время, память и относительное время (по отношению к quicksort).
    Для каждого размера массива и типа данных показывает результаты всех алгоритмов.
    """
    print("ДЕТАЛЬНЫЙ АНАЛИЗ РЕЗУЛЬТАТОВ")
    print("=" * 100)

    for size in sizes:
        print(f"\nРАЗМЕР МАССИВА: {size}")
        print("-" * 80)
        for case_type in ['random', 'sorted', 'reverse']:
            print(f"\nТип данных: {case_type}")
            print(f"Алгоритм\tВремя (с)\tПамять (Б)\tОтносительное время")
            print("-" * 60)
            base_time = results[size][case_type]['quicksort']['time']
            for alg_name in ['quicksort', 'insertion_sort', 'merge_sort', 'heap_sort']:
                time_val = results[size][case_type][alg_name]['time']
                memory_val = results[size][case_type][alg_name]['memory']
                relative_time = time_val / base_time if base_time > 0 else float('inf')
                print(f"{alg_name}\t{time_val:.6f}\t{memory_val:.0f}\t\t{relative_time:.2f}x")


def main():
    """
    Основная функция программы:
    1. Задаёт размеры массивов для тестирования.
    2. Устанавливает количество повторений для усреднения результатов (num_runs).
    3. Запускает эксперимент через вызов run_experiment().
    4. Выводит подробные результаты с помощью print_detailed_results().
    5. Строит графики производительности с помощью plot_results().
    """
    sizes = [10, 50, 100, 500, 1000]
    num_runs = 10  # Количество повторений
    print(f"Запуск эксперимента с {num_runs} повторениями для каждого теста...")
    results = run_experiment(sizes, num_runs)
    print_detailed_results(results, sizes)
    plot_results(results, sizes)


if __name__ == "__main__":
    main()
