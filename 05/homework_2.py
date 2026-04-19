# Напишите рекурсивную функцию для нахождения максимального
# элемента в списке, используя подход "Разделяй и властвуй".


import random
import time


def find_max_dac(lst):
    """Вариант 1: работа с копиями списков"""
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    max_left = find_max_dac(left_half)
    max_right = find_max_dac(right_half)
    return max(max_left, max_right)


def find_max_optimized(lst, start=0, end=None):
    """Вариант 2: работа с индексами (оптимизированный)"""
    if end is None:
        end = len(lst) - 1
    if start == end:
        return lst[start]
    mid = (start + end) // 2
    max_left = find_max_optimized(lst, start, mid)
    max_right = find_max_optimized(lst, mid + 1, end)
    return max(max_left, max_right)


def measure_execution_time(func, *args, **kwargs):
    """
    Обёрточная функция для замера времени выполнения любой функции.
    Параметры:
    - func: функция, время выполнения которой нужно замерить.
    - *args: позиционные аргументы для функции.
    - **kwargs: именованные аргументы для функции.
    Возвращает:
    - result: результат выполнения функции.
    - execution_time: время выполнения в секундах.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


# Основной код программы
if __name__ == "__main__":
    # Запрос количества элементов
    n = int(input("Введите количество элементов списка для тестирования: "))

    # Заполнение списка случайными числами (от 1 до 1000)
    test_list = [random.randint(1, 1000) for _ in range(n)]

    print(f"\nСгенерированный список ({n} элементов):")
    print(test_list)

    # Тестирование вариантов с использованием обёртки
    result1, time1 = measure_execution_time(find_max_dac, test_list)
    result2, time2 = measure_execution_time(find_max_optimized, test_list)

    # Вывод результатов
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("="*50)
    print(f"Максимум (вариант 1 — с копиями списков): {result1}")
    print(f"Время выполнения (вариант 1): {time1:.6f} секунд")
    print("-"*50)
    print(f"Максимум (вариант 2 — с индексами): {result2}")
    print(f"Время выполнения (вариант 2): {time2:.6f} секунд")
    print("="*50)

    # Сравнение производительности
    if time1 > 0 and time2 > 0:
        speedup = time1 / time2
        if speedup > 1:
            print(f"Вариант 2 быстрее варианта 1 в {speedup:.2f} раза")
        elif speedup < 1:
            print(f"Вариант 1 быстрее варианта 2 в {1/speedup:.2f} раза")
        else:
            print("Оба варианта показали одинаковую скорость")
