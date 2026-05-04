# Реализуйте алгоритм Флойда-Уоршелла для нахождения кратчайших путей между всеми парами вершин в графе,
# представленного в виде матрицы смежности.


import sys


def floyd_warshall(graph):
    """
    Реализация алгоритма Флойда-Уоршелла.
    Args:
        graph: матрица смежности графа. Отсутствие ребра обозначается INF.
    Returns:
        Матрица кратчайших расстояний между всеми парами вершин.
    """
    # Количество вершин в графе
    V = len(graph)

    # Константа для обозначения отсутствия ребра (бесконечность)
    INF = sys.maxsize

    # Создаём копию матрицы для хранения результатов
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # Основной цикл алгоритма
    for k in range(V):  # Промежуточная вершина
        for i in range(V):  # Начальная вершина
            for j in range(V):  # Конечная вершина
                # Проверяем, существует ли путь через вершину k
                if (dist[i][k] != INF and dist[k][j] != INF
                        and dist[i][k] + dist[k][j] < dist[i][j]):
                    # Обновляем расстояние, если найден более короткий путь
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_solution(dist):
    """Вспомогательная функция для вывода результата."""
    V = len(dist)
    print("Матрица кратчайших расстояний:")
    for i in range(V):
        row = []
        for j in range(V):
            if dist[i][j] == sys.maxsize:
                row.append("INF")
            else:
                row.append(str(dist[i][j]))
        print(" ".join(row))


# Пример графа с 4 вершинами
# INF означает отсутствие прямого ребра
INF = sys.maxsize
graph = [
    [0,   3,   INF, 7  ],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1  ],
    [2,   INF, INF, 0  ]
]

# Запускаем алгоритм
result = floyd_warshall(graph)

# Выводим результат
print_solution(result)
