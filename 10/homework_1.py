# Реализуйте функцию, решающую задачу о рюкзаке с помощью динамического программирования. Вам дан рюкзак с
# определенной вместимостью и набор предметов с заданными весами и стоимостями. Необходимо найти максимальную
# стоимость предметов, которые можно поместить в рюкзак.


def knapsack(capacity, weights, values):
    """
    Решает задачу о рюкзаке методом динамического программирования.
    Args:
        capacity (int): вместимость рюкзака
        weights (list): список весов предметов
        values (list): список стоимостей предметов
    Returns:
        tuple: (максимальная стоимость, список индексов выбранных предметов)
    """
    n = len(values)

    # Создаём таблицу DP: dp[i][w] — макс. стоимость для первых i предметов и вместимости w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Заполняем таблицу DP
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Вес текущего предмета
            weight = weights[i - 1]
            # Стоимость текущего предмета
            value = values[i - 1]

            if weight <= w:
                # Берём максимум из:
                # 1. Не берём текущий предмет: dp[i-1][w]
                # 2. Берём текущий предмет: value + dp[i-1][w-weight]
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])
            else:
                # Предмет не помещается — берём значение из предыдущей строки
                dp[i][w] = dp[i - 1][w]

    # Восстанавливаем набор выбранных предметов
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # Если значение отличается от предыдущей строки, предмет был выбран
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # добавляем индекс предмета
            w -= weights[i - 1]  # уменьшаем оставшуюся вместимость

    selected_items.reverse()  # восстанавливаем порядок выбора

    return dp[n][capacity], selected_items


# Пример использования
if __name__ == "__main__":
    # Вместимость рюкзака
    capacity = 50

    # Веса предметов
    weights = [10, 20, 30]
    # Стоимости предметов
    values = [60, 100, 120]

    max_value, selected = knapsack(capacity, weights, values)

    print(f"Максимальная стоимость: {max_value}")
    print(f"Выбранные предметы (индексы): {selected}")

    # Подробная информация о выбранных предметах
    print("\nВыбранные предметы:")
    total_weight = 0
    for idx in selected:
        print(f"  Предмет {idx}: вес={weights[idx]}, стоимость={values[idx]}")
        total_weight += weights[idx]
    print(f"Общий вес: {total_weight}/{capacity}")
