# Напишите класс BinaryTree, который реализует основные операции бинарного дерева:
# вставка (insert) и поиск (search).


import matplotlib.pyplot as plt
import networkx as nx


class BinaryTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка значения в бинарное дерево поиска."""
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Рекурсивная вставка значения в поддерево."""
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)
        # Дубликаты игнорируются

    def search(self, value):
        """Поиск значения в бинарном дереве поиска."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Рекурсивный поиск значения в поддереве."""
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:  # value > node.value
            return self._search_recursive(node.right, value)

    def visualize_with_matplotlib(self, figsize=(12, 8), node_size=1500,
                              node_color='lightblue', font_size=12):
        """
        Визуализирует дерево с помощью matplotlib и networkx.
        Параметры:
        - figsize: размер фигуры (ширина, высота)
        - node_size: размер узлов
        - node_color: цвет узлов
        - font_size: размер шрифта для значений
        """
        # Создаём направленный граф
        G = nx.DiGraph()
        pos = {}  # Позиции узлов
        labels = {}  # Метки узлов

        # Если дерево пустое
        if self.root is None:
            plt.figure(figsize=figsize)
            plt.text(0.5, 0.5, 'Дерево пустое',
                    ha='center', va='center', fontsize=16, color='red')
            plt.axis('off')
            plt.show()
            return

        # Функция для обхода дерева и добавления узлов и рёбер
        def add_nodes(node, parent_id=None, x=0, y=0, depth=0):
            if node is not None:
                # Уникальный идентификатор узла
                node_id = id(node)

                # Добавляем узел в граф
                G.add_node(node_id)
                labels[node_id] = node.value

                # Позиция узла (с учётом глубины для вертикального расположения)
                pos[node_id] = (x, -depth)

                # Добавляем ребро от родителя к текущему узлу
                if parent_id is not None:
                    G.add_edge(parent_id, node_id)

                # Рекурсивно добавляем левое и правое поддеревья
                # Сдвигаем позиции для избежания наложения узлов
                spacing = 1 / (depth + 1)
                add_nodes(node.left, node_id, x - spacing, depth + 1, depth + 1)
                add_nodes(node.right, node_id, x + spacing, depth + 1, depth + 1)

        # Запускаем обход с корня
        add_nodes(self.root)

        # Визуализация
        plt.figure(figsize=figsize)
        nx.draw(G, pos, labels=labels, with_labels=True,
                node_size=node_size, node_color=node_color,
                font_size=font_size, font_weight='bold',
                arrows=True, arrowstyle='->', arrowsize=20)
        plt.title("Бинарное дерево поиска", fontsize=16, fontweight='bold')
        plt.axis('off')
        # Настраиваем отступы: left, bottom, right, top
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.show()


# Пример использования
if __name__ == "__main__":
    # Создаём дерево и добавляем элементы
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8, 1, 9]

    for value in values:
        tree.insert(value)

    # Проверяем поиск
    print("Поиск 4:", tree.search(4))  # True
    print("Поиск 10:", tree.search(10))  # False

    # Визуализируем дерево
    tree.visualize_with_matplotlib(
        figsize=(14, 10),
        node_size=2000,
        node_color='lightgreen',
        font_size=14
    )
