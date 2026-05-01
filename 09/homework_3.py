# Напишите функцию для создания матрицы смежности из списка ребер.
# Реализуйте функции для добавления вершины и ребра в граф, представленный в виде матрицы смежности.


def create_adjacency_matrix(num_vertices, edges, directed=False):
    """
    Создаёт матрицу смежности из списка рёбер.
    Параметры:
    - num_vertices: количество вершин в графе (вершины нумеруются от 0 до num_vertices-1)
    - edges: список кортежей (u, v), представляющих рёбра
    - directed: флаг, указывающий, является ли граф ориентированным
    Возвращает:
    - матрицу смежности (двумерный список)
    """
    # Инициализируем матрицу нулями размером num_vertices × num_vertices
    matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Заполняем матрицу на основе рёбер
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:  # Для неориентированного графа добавляем обратное ребро
            matrix[v][u] = 1

    return matrix



class Graph:
    def __init__(self, directed=False):
        """
        Инициализация графа.
        Параметры:
        - directed: флаг, указывающий, является ли граф ориентированным
        """
        self.matrix = []  # Матрица смежности
        self.num_vertices = 0  # Количество вершин
        self.directed = directed  # Тип графа

    def add_vertex(self):
        """
        Добавляет новую вершину в граф.
        """
        # Увеличиваем размер матрицы на 1×1
        for row in self.matrix:
            row.append(0)  # Добавляем столбец для новой вершины

        # Добавляем новую строку для новой вершины
        new_row = [0] * (self.num_vertices + 1)
        self.matrix.append(new_row)

        self.num_vertices += 1

    def add_edge(self, u, v):
        """
        Добавляет ребро между вершинами u и v.
        Параметры:
        - u: индекс первой вершины
        - v: индекс второй вершины
        """
        # Проверяем, что вершины существуют
        if u >= self.num_vertices or v >= self.num_vertices:
            raise ValueError("Одна или обе вершины не существуют в графе")

        # Устанавливаем связь между вершинами
        self.matrix[u][v] = 1
        if not self.directed:  # Для неориентированного графа добавляем обратное ребро
            self.matrix[v][u] = 1

    def display_matrix(self):
        """
        Выводит матрицу смежности в читаемом формате.
        """
        print("Матрица смежности:")
        for i, row in enumerate(self.matrix):
            print(f"Вершина {i}: {row}")



# Пример использования всех функций
if __name__ == "__main__":
    print("=== Пример 1: Создание матрицы смежности из списка рёбер ===")
    # Пример для неориентированного графа
    num_vertices = 4
    edges = [(0, 1), (1, 2), (1, 3), (2, 3)]
    adj_matrix = create_adjacency_matrix(num_vertices, edges)

    print("Матрица смежности для графа с рёбрами (0,1), (1,2), (1,3), (2,3):")
    for row in adj_matrix:
        print(row)

    print("\n=== Пример 2: Работа с классом Graph ===")
    # Создаём граф
    graph = Graph(directed=False)  # Неориентированный граф

    # Добавляем вершины (по одной)
    print("Добавляем 3 вершины...")
    for _ in range(3):
        graph.add_vertex()

    # Добавляем рёбра
    print("Добавляем рёбра (0,1) и (1,2)...")
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)

    print("После добавления вершин и рёбер:")
    graph.display_matrix()

    # Добавляем ещё одну вершину
    print("\nДобавляем ещё одну вершину...")
    graph.add_vertex()
    print("После добавления ещё одной вершины:")
    graph.display_matrix()

    # Добавляем ребро с новой вершиной
    print("\nДобавляем ребро (2,3)...")
    graph.add_edge(2, 3)
    print("После добавления ребра (2,3):")
    graph.display_matrix()

    print("\n=== Пример 3: Ориентированный граф ===")
    # Создаём ориентированный граф
    directed_graph = Graph(directed=True)

    # Добавляем 3 вершины
    print("Добавляем 3 вершины в ориентированный граф...")
    for _ in range(3):
        directed_graph.add_vertex()

    # Добавляем направленные рёбра
    print("Добавляем направленные рёбра (0→1), (1→2), (2→0)...")
    directed_graph.add_edge(0, 1)
    directed_graph.add_edge(1, 2)
    directed_graph.add_edge(2, 0)

    print("Матрица смежности ориентированного графа:")
    directed_graph.display_matrix()
