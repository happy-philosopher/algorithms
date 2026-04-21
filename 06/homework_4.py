# Проанализируйте время выполнения сортировки слиянием на списках различной длины (например, 10, 100, 1000 элементов)
# и сравните её с другими сортировками, такими как сортировка пузырьком.


import time
import random
import matplotlib.pyplot as plt


# Алгоритм сортировки слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
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


# Алгоритм пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Алгоритм быстрой сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Функция для замера времени выполнения
def measure_time(sort_func, data):
    start_time = time.time()
    sorted_data = sort_func(data.copy())
    end_time = time.time()
    return end_time - start_time


# Основные параметры тестирования
sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]

# Словарь для хранения результатов
results = {
    'merge_sort': [],
    'bubble_sort': [],
    'quick_sort': []
}

# Проведение замеров для каждого размера списка
for size in sizes:
    # Создаём случайный список заданной длины
    random_data = [random.randint(1, 10000) for _ in range(size)]

    # Замер времени для сортировки слиянием
    merge_time = measure_time(merge_sort, random_data)
    results['merge_sort'].append(merge_time)

    # Замер времени для пузырьковой сортировки
    bubble_time = measure_time(bubble_sort, random_data)
    results['bubble_sort'].append(bubble_time)

    # Замер времени для быстрой сортировки
    quick_time = measure_time(quick_sort, random_data)
    results['quick_sort'].append(quick_time)

# Вывод результатов в табличном виде
print("Результаты замеров времени (в секундах):")
print(f"{'Размер':<6} {'Сортировка слиянием':<20} {'Пузырьковая':<12} {'Быстрая сортировка':<18}")
print("-" * 65)

for i, size in enumerate(sizes):
    print(f"{size:<8} {results['merge_sort'][i]:<18.6f} {results['bubble_sort'][i]:<15.6f} {results['quick_sort'][i]:<18.6f}")

# Построение графика сравнения
plt.figure(figsize=(12, 7))
plt.plot(sizes, results['merge_sort'], label='Сортировка слиянием', marker='o')
plt.plot(sizes, results['bubble_sort'], label='Пузырьковая сортировка', marker='s')
plt.plot(sizes, results['quick_sort'], label='Быстрая сортировка', marker='^')

plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (секунды)')
plt.title('Сравнение времени выполнения различных алгоритмов сортировки')
plt.legend()
plt.grid(True, alpha=0.3)
plt.yscale('log')  # Логарифмическая шкала для лучшей визуализации
plt.tight_layout()
plt.show()

# Дополнительный анализ и выводы
print("\n" + "=" * 65)
print("АНАЛИЗ РЕЗУЛЬТАТОВ:")
print("=" * 65)

print("1. Сортировка слиянием (Merge Sort):")
print("   - Стабильное время выполнения O(n log n)")
print("   - Предсказуемая производительность на любых данных")
print("   - Требует дополнительной памяти O(n)")

print("\n2. Пузырьковая сортировка (Bubble Sort):")
print("   - Квадратичная сложность O(n²)")
print("   - Резкий рост времени при увеличении размера данных")
print("   - Практическое применение ограничено малыми массивами")

print("\n3. Быстрая сортировка (Quick Sort):")
print("   - Средняя сложность O(n log n), худший случай O(n²)")
print("   - Обычно работает быстрее сортировки слиянием")
print("   - Не требует дополнительной памяти (in-place)")
print("   - Производительность зависит от выбора опорного элемента")

print("\nВЫВОДЫ:")
print("- Для малых массивов (< 100 элементов) разница между алгоритмами незначительна")
print("- При увеличении размера данных пузырьковая сортировка становится неприемлемо медленной")
print("- Сортировка слиянием и быстрая сортировка показывают хорошую масштабируемость")
print("- Быстрая сортировка часто оказывается самой быстрой на практике")
