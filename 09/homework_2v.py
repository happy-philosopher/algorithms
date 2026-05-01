# Задача № 2, добавлена визуализация
# Нужно установить: pip install scipy


import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


def bfs_with_visualization(graph, start):
    """
    Обход ориентированного графа в ширину с визуализацией.
    Args:
        graph: словарь, где ключи — вершины, значения — списки соседних вершин.
        start: стартовая вершина для обхода.
    """
    # Создаём ориентированный граф NetworkX
    G = nx.DiGraph()

    # Добавляем рёбра в граф
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Позиции вершин для визуализации (используем раскладку Kamada-Kawai)
    pos = nx.kamada_kawai_layout(G)

    # Множества для отслеживания состояния вершин
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    # Настройка визуализации
    plt.figure(figsize=(12, 8))

    step = 0
    print("Пошаговый обход BFS:")

    while queue:
        step += 1
        vertex = queue.popleft()
        result.append(vertex)
        print(f"Шаг {step}: посещена вершина '{vertex}'")

        # Визуализация текущего состояния
        plt.clf()  # Очищаем предыдущее изображение

        # Определяем цвета вершин
        node_colors = []
        for node in G.nodes():
            if node == vertex:  # Текущая обрабатываемая вершина
                node_colors.append('red')
            elif node in visited:  # Уже посещённые вершины
                node_colors.append('green')
            elif node in queue:  # Вершины в очереди
                node_colors.append('yellow')
            else:  # Непосещённые вершины
                node_colors.append('lightblue')

        # Рисуем граф
        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1500,
            font_size=16,
            arrows=True,
            arrowsize=20,
            edge_color='gray'
        )

        # Добавляем заголовок с информацией о текущем шаге
        plt.title(f"BFS обход — шаг {step}\n"
                  f"Текущая вершина: '{vertex}', "
                  f"Очередь: {list(queue)}, "
                  f"Посещённые: {sorted(visited)}",
                  fontsize=14)

        # Отображаем текущее состояние
        plt.pause(2)  # Пауза 2 секунды между шагами

        # Обрабатываем соседние вершины
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Финальная визуализация — все вершины посещены
    plt.clf()
    nx.draw(
        G, pos,
        with_labels=True,
        node_color='green',
        node_size=1500,
        font_size=16,
        arrows=True,
        arrowsize=20,
        edge_color='gray'
    )
    plt.title("BFS обход завершён!\n"
              f"Порядок посещения: {result}",
              fontsize=16)
    plt.show()

    return result


# Пример:
# Создаём ориентированный граф
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Запускаем BFS с визуализацией с вершины 'A'
result = bfs_with_visualization(graph, 'A')
print("\nИтоговый порядок посещения вершин:", result)
