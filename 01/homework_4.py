# Сравните время выполнения линейного поиска для разных размеров списков (например,
# 10, 100, 1000 элементов). Постройте график зависимости времени выполнения от размера списка.

# Работа программы занимает примерно 35 сек, подождите в конце появится график.


import random
import time
import matplotlib.pyplot as plt


def linear_search(arr, target):
    """Линейный поиск элемента в списке."""
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def measure_search_time(arr, target):
    """Измеряет время выполнения линейного поиска."""
    start_time = time.perf_counter()
    result = linear_search(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time, result


# Параметры тестирования
sizes = [20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
# sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []
num_trials = 100  # Количество повторений для усреднения

print("Результаты тестирования:\n")
for size in sizes:
    # Создаём список случайных чисел и сортируем его
    arr = sorted(random.sample(range(1, size * 10), size))
    # Ищем последний элемент (худший случай)
    target = arr[-1]
    total_time = 0
    for _ in range(num_trials):
        search_time, _ = measure_search_time(arr, target)
        total_time += search_time
    average_time = total_time / num_trials
    times.append(average_time)
    print(f"Размер: {size:5d} элементов | Среднее время: {average_time:.8f} сек")

# Построение графика
plt.figure(figsize=(12, 7))
plt.plot(sizes, times, marker='o', linestyle='-', linewidth=2, markersize=8, color='#2E86AB')
plt.title('Зависимость времени выполнения линейного поиска от размера списка', fontsize=14, fontweight='bold')
plt.xlabel('Размер списка', fontsize=12)
plt.ylabel('Среднее время выполнения (секунды)', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(sizes)
# plt.yscale('log')  # Шкала логарифмическая

# Добавляем подписи значений на точках
for i, (size, time_val) in enumerate(zip(sizes, times)):
    plt.annotate(f'{time_val:.6f}', (size, time_val),
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

plt.tight_layout()
plt.show()

# Вывод теоретической сложности
print(f"\nТеоретическая сложность линейного поиска: O(n)")
print(f"Ожидаемое поведение: время пропорционально размеру списка")
