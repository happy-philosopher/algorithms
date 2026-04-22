# Напишите функцию, которая принимает строку и возвращает её хеш-значение.
# Для этого используйте простой алгоритм: сложение ASCII-кодов всех символов строки.


def simple_hash(string):
    """
    Вычисляет хеш-значение строки как сумму ASCII-кодов всех символов.
    Args:
        string (str): входная строка для хеширования.
    Returns:
        int: хеш-значение — сумма ASCII-кодов символов строки.
    """
    hash_value = 0
    for char in string:
        hash_value += ord(char)
    return hash_value


# Пример:
print(simple_hash("abc"))
print(simple_hash("Hello"))
print(simple_hash(""))
print(simple_hash("A"))
