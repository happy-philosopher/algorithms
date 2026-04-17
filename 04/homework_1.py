# Напишите рекурсивную функцию для вычисления факториала числа n.


def factorial(n):
    # Базовый случай: факториал 0 и 1 равен 1
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    # Рекурсивный случай: n# = n * (n-1)!
    else:
        return n * factorial(n - 1)


# Пример использования
n = int(input("Введите число n: "))
result = factorial(n)
print(f"Факториал числа {n} равен {result}")
