# Напишите функцию для обхода ориентированного графа в ширину (Breadth-First Search, BFS).


from collections import deque


def bfs(graph, start):
    """
    Обход ориентированного графа в ширину (BFS).
    Args:
        graph: словарь, где ключи — вершины, значения — списки соседних вершин.
        start: стартовая вершина для обхода.
    Returns:
        Список вершин в порядке их посещения.
    """
    # Множество для хранения посещённых вершин
    visited = set()
    # Очередь для BFS
    queue = deque([start])
    # Список для хранения порядка посещения вершин
    result = []

    # Помечаем стартовую вершину как посещённую
    visited.add(start)

    while queue:
        # Извлекаем вершину из начала очереди
        vertex = queue.popleft()
        # Добавляем вершину в результат
        result.append(vertex)

        # Проверяем все соседние вершины
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                # Помечаем как посещённую и добавляем в очередь
                visited.add(neighbor)
                queue.append(neighbor)

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

# Запускаем BFS с вершины 'A'
result = bfs(graph, 'A')
print("Порядок посещения вершин:", result)
