# Напишите рекурсивную функцию для вычисления n-го числа
# Фибоначчи и проанализируйте стек вызовов для n = 5.


def fibonacci(n):
    # Базовые случаи: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Рекурсивный случай: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


# Пример вызова для n = 5
print(fibonacci(5))  # Вывод: 5


"""
Анализ стека вызовов для n = 5
-------------------------------

Разберём пошагово, как работает функция при вызове fibonacci(5). Стек вызовов — это структура данных, 
где каждый новый вызов функции добавляется на вершину стека, а после завершения — удаляется.

Шаг 1. Вызов fibonacci(5):
Поскольку n>1, функция вызывает fibonacci(4) и fibonacci(3).
Стек: [fibonacci(5)] → [fibonacci(5), fibonacci(4)].

Шаг 2. Вызов fibonacci(4):
n>1, вызываем fibonacci(3) и fibonacci(2).
Стек: [fibonacci(5), fibonacci(4)] → [fibonacci(5), fibonacci(4), fibonacci(3)].

Шаг 3. Вызов fibonacci(3) (из fibonacci(4)):
n>1, вызываем fibonacci(2) и fibonacci(1).
Стек: [fibonacci(5), fibonacci(4), fibonacci(3)] → [fibonacci(5), fibonacci(4), fibonacci(3), fibonacci(2)].

Шаг 4. Вызов fibonacci(2) (из fibonacci(3)):
n>1, вызываем fibonacci(1) и fibonacci(0).
Стек: [fibonacci(5), fibonacci(4), fibonacci(3), fibonacci(2)] → [fibonacci(5), fibonacci(4), fibonacci(3), 
fibonacci(2), fibonacci(1)].

Шаг 5. Вызов fibonacci(1):
Базовый случай: возвращаем 1.
Стек: [fibonacci(5), fibonacci(4), fibonacci(3), fibonacci(2), fibonacci(1)] → [fibonacci(5), fibonacci(4), 
fibonacci(3), fibonacci(2)].

Шаг 6. Вызов fibonacci(0):
*Базовый случай: возвращаем 0.
Стек: [fibonacci(5), fibonacci(4), fibonacci(3), fibonacci(2)] → [fibonacci(5), fibonacci(4), fibonacci(3)].
fibonacci(2) возвращает 1+0=1.

Шаг 7. Вызов fibonacci(1) (из fibonacci(3)):
*Базовый случай: возвращаем 1.
Стек: [fibonacci(5), fibonacci(4), fibonacci(3)] → [fibonacci(5), fibonacci(4)].
fibonacci(3) возвращает 1+1=2.

Шаг 8. Вызов fibonacci(2) (из fibonacci(4)):
Аналогично шагу 4, возвращает 1.
Стек: [fibonacci(5), fibonacci(4)] → [fibonacci(5)].
fibonacci(4) возвращает 2+1=3.

Шаг 9. Вызов fibonacci(3) (из fibonacci(5)):
Уже вычислено ранее (шаг 7), возвращает 2.
Стек: [fibonacci(5)] → [].
fibonacci(5) возвращает 3+2=5.


Дерево вызовов для fibonacci(5) выглядит так:

fibonacci(5)
├── fibonacci(4)
│   ├── fibonacci(3)
│   │   ├── fibonacci(2)
│   │   │   ├── fibonacci(1) → 1
│   │   │   └── fibonacci(0) → 0
│   │   └── fibonacci(1) → 1
│   └── fibonacci(2)
│       ├── fibonacci(1) → 1
│       └── fibonacci(0) → 0
└── fibonacci(3)
    ├── fibonacci(2)
    │   ├── fibonacci(1) → 1
    │   └── fibonacci(0) → 0
    └── fibonacci(1) → 1

Итоговые значения:
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(2) = 1
fibonacci(3) = 2
fibonacci(4) = 3
fibonacci(5) = 5

ВЫВОДЫ
-------
1. Избыточные вычисления. В рекурсивном подходе одни и те же значения (например, fibonacci(2) или fibonacci(3))
    вычисляются многократно. Это делает алгоритм неэффективным для больших n.
2. Сложность. Временная сложность — O(2**n), пространственная — O(n) (из‑за глубины стека).
3. Оптимизация. Для повышения эффективности можно использовать:
    - Мемоизацию (кэширование результатов).
    - Итеративный подход (цикл вместо рекурсии).
"""