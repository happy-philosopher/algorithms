# Создайте список из 100 случайных чисел и выполните линейный
# поиск для нескольких различных значений. Запишите результаты.


import random

def linear_search(lst, target):
    """
    Линейный поиск элемента в списке.
    Возвращает индекс элемента, если найден, иначе -1.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


# Устанавливаем seed для воспроизводимости результатов
random.seed(88)

# Значения для поиска (некоторые есть в списке, некоторых нет)
search_values = [42, 151, 503, 999, 85]

# Создаём список из 100 случайных целых чисел в диапазоне от 1 до 1000
random_numbers = [random.randint(1, 1000) for _ in range(100)]
print("Список из 100 случайных чисел:")
print(random_numbers)
print("\n" + "=" * 50 + "\n")

print("Результаты линейного поиска:")
print("-" * 30)
for value in search_values:
    result = linear_search(random_numbers, value)
    if result != -1:
        print(f"Значение {value} найдено на позиции {result} (индекс {result})")
    else:
        print(f"Значение {value} не найдено в списке")
