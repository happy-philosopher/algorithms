# Задача № 1, добавлена визуализация


import matplotlib.pyplot as plt
import networkx as nx

class DirectedGraph:
    def __init__(self):
        """Инициализация графа: создаём словарь для хранения вершин и их соседей."""
        self.vertices = {}
        # Внутренний граф NetworkX для визуализации
        self._nx_graph = nx.DiGraph()

    def add_vertex(self, vertex):
        """
        Добавляет вершину в граф, если её ещё нет.
        Args:
            vertex: идентификатор вершины (может быть числом, строкой и т. д.)
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            self._nx_graph.add_node(vertex)

    def add_edge(self, from_vertex, to_vertex):
        """
        Добавляет ориентированное ребро от from_vertex к to_vertex.
        Args:
            from_vertex: начальная вершина ребра
            to_vertex: конечная вершина ребра
        Raises:
            ValueError: если одна из вершин не существует в графе
        """
        # Проверяем, существуют ли обе вершины
        if from_vertex not in self.vertices:
            raise ValueError(f"Вершина {from_vertex} не существует в графе")
        if to_vertex not in self.vertices:
            raise ValueError(f"Вершина {to_vertex} не существует в графе")

        # Добавляем ребро (ориентированное)
        self.vertices[from_vertex].add(to_vertex)
        self._nx_graph.add_edge(from_vertex, to_vertex)

    def get_vertices(self):
        """Возвращает список всех вершин графа."""
        return list(self.vertices.keys())

    def get_edges(self):
        """Возвращает список всех рёбер графа в виде кортежей (from, to)."""
        edges = []
        for from_vertex, neighbors in self.vertices.items():
            for to_vertex in neighbors:
                edges.append((from_vertex, to_vertex))
        return edges

    def has_vertex(self, vertex):
        """Проверяет, существует ли вершина в графе."""
        return vertex in self.vertices

    def has_edge(self, from_vertex, to_vertex):
        """Проверяет, существует ли ориентированное ребро от from_vertex к to_vertex."""
        if from_vertex not in self.vertices:
            return False
        return to_vertex in self.vertices[from_vertex]

    def visualize(self, title="Ориентированный граф", figsize=(10, 8)):
        """
        Визуализирует граф с помощью matplotlib и networkx.
        Args:
            title: заголовок графика
            figsize: размер фигуры (ширина, высота)
        """
        plt.figure(figsize=figsize)

        # Определяем позиции узлов (вершин)
        pos = nx.spring_layout(self._nx_graph, seed=42)

        # Рисуем граф
        nx.draw(
            self._nx_graph,
            pos,
            with_labels=True,
            node_color='lightblue',
            node_size=1500,
            font_size=16,
            font_weight='bold',
            arrowsize=20,
            edge_color='gray',
            width=2,
            arrows=True
        )

        plt.title(title, fontsize=18, fontweight='bold')
        plt.axis('off')
        plt.show()

    def __str__(self):
        """Строковое представление графа для удобного вывода."""
        result = "Ориентированный граф:\n"
        for vertex, neighbors in self.vertices.items():
            if neighbors:
                result += f"  {vertex} -> {', '.join(map(str, neighbors))}\n"
            else:
                result += f"  {vertex} (нет исходящих рёбер)\n"
        return result


def test_directed_graph_with_visualization():
    print("=== Тестирование класса DirectedGraph с визуализацией ===\n")

    # Создаём граф
    graph = DirectedGraph()

    # Добавляем вершины
    print("1. Добавляем вершины A, B, C, D, E:")
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    print(graph)
    graph.visualize("Шаг 1: Только вершины")

    # Добавляем рёбра
    print("2. Добавляем ориентированные рёбра:")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("D", "E")
    print(graph)
    graph.visualize("Шаг 2: Добавлены рёбра")

    # Проверяем наличие вершин и рёбер
    print("3. Проверяем наличие элементов:")
    print(f"  Вершина 'A' существует: {graph.has_vertex('A')}")
    print(f"  Вершина 'X' существует: {graph.has_vertex('X')}")
    print(f"  Ребро A->B существует: {graph.has_edge('A', 'B')}")
    print(f"  Ребро B->A существует: {graph.has_edge('B', 'A')}")  # Должно быть False
    print()

    # Получаем списки вершин и рёбер
    print("4. Списки вершин и рёбер:")
    print(f"  Вершины: {graph.get_vertices()}")
    print(f"  Рёбра: {graph.get_edges()}")
    print()

    # Попытка добавить ребро с несуществующей вершиной
    print("5. Попытка добавить ребро с несуществующей вершиной (должно вызвать ошибку):")
    try:
        graph.add_edge("A", "X")
    except ValueError as e:
        print(f"  Поймана ошибка: {e}")


if __name__ == "__main__":
    test_directed_graph_with_visualization()
