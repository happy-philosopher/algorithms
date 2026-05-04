# Реализуйте функцию, которая находит длину наибольшей общей подпоследовательности (LCS) двух строк.


def lcs_length(str1, str2):
    """
    Находит длину наибольшей общей подпоследовательности двух строк.
    Args:
        str1 (str): Первая строка.
        str2 (str): Вторая строка.
    Returns:
        int: Длина наибольшей общей подпоследовательности.
    """
    m, n = len(str1), len(str2)

    # Создаём таблицу DP размером (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Заполняем таблицу DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Если символы совпадают, увеличиваем длину LCS на 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Иначе берём максимальное значение из соседних ячеек
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Пример использования
if __name__ == "__main__":
    string1 = "ABCDGH"
    string2 = "AEDFHR"
    result = lcs_length(string1, string2)
    print(f"Длина LCS строк '{string1}' и '{string2}': {result}")
