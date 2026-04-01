# Реализуйте алгоритм линейного поиска на языке Python. Функция должна принимать список и
# элемент для поиска, и возвращать индекс элемента или -1, если элемент не найден.


def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1


lst_m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search(lst_m, 10))
