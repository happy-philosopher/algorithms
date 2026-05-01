# Напишите функции для создания списка смежности из списка ребер.
# Реализуйте функции для добавления вершины и ребра в граф, представленный в виде списка смежности.


class Graph:
    def __init__(self, directed=False):
        """
        Инициализирует граф.
        Args:
            directed: True для ориентированного графа
        """
        self.adjacency_list = {}
        self.directed = directed

    def create_from_edges(self, edges):
        """
        Создаёт граф из списка рёбер.
        Args:
            edges: список кортежей (вершина1, вершина2)
        """
        for v1, v2 in edges:
            self.add_edge(v1, v2)

    def add_vertex(self, vertex):
        """
        Добавляет вершину в граф.
        Args:
            vertex: добавляемая вершина
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        """
        Добавляет ребро в граф.
        Args:
            v1: первая вершина
            v2: вторая вершина
        """
        # Убеждаемся, что обе вершины существуют
        self.add_vertex(v1)
        self.add_vertex(v2)

        # Добавляем ребро от v1 к v2
        self.adjacency_list[v1].append(v2)

        # Для неориентированного графа добавляем обратное ребро
        if not self.directed:
            self.adjacency_list[v2].append(v1)

    def get_adjacency_list(self):
        """Возвращает текущий список смежности."""
        return self.adjacency_list


# Пример использования:
# Создаём неориентированный граф
g = Graph(directed=False)

# Заполняем рёбрами
edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
g.create_from_edges(edges)

print("Граф после создания:", g.get_adjacency_list())
# Вывод: {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

# Добавляем вершину и ребро
g.add_vertex(4)
g.add_edge(1, 4)

print("Финальный граф:", g.get_adjacency_list())
# Вывод: {0: [1, 3], 1: [0, 2, 4], 2: [1, 3], 3: [0, 2], 4: [1]}
