# Напишите класс AVLTree, который наследует класс BinaryTree и добавляет операции балансировки
# при вставке элементов. Реализуйте методы для поворотов (left_rotate, right_rotate)
# и балансировки (rebalance).


import matplotlib.pyplot as plt
import networkx as nx
import random

# Базовый класс бинарного дерева поиска (без балансировки)
class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        # Случайный выбор направления вставки (для создания случайного несбалансированного дерева)
        go_left = random.choice([True, False])

        if go_left:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)

    def visualize_with_matplotlib(self, title="Бинарное дерево поиска", figsize=(12, 8)):
        G = nx.DiGraph()
        pos = {}
        labels = {}

        if self.root is None:
            plt.figure(figsize=figsize)
            plt.text(0.5, 0.5, 'Дерево пустое',
                    ha='center', va='center', fontsize=16, color='red')
            plt.axis('off')
            plt.title(title, fontsize=14, fontweight='bold')
            plt.show()
            return

        def add_nodes(node, parent_id=None, x=0, depth=0):
            if node is not None:
                node_id = id(node)
                G.add_node(node_id)
                labels[node_id] = node.value
                pos[node_id] = (x, -depth)
                if parent_id is not None:
                    G.add_edge(parent_id, node_id)
                spacing = 1 / (depth + 1)
                add_nodes(node.left, node_id, x - spacing, depth + 1)
                add_nodes(node.right, node_id, x + spacing, depth + 1)

        add_nodes(self.root)

        plt.figure(figsize=figsize)
        nx.draw(G, pos, labels=labels, with_labels=True,
                node_size=1500, node_color='lightcoral',
                font_size=12, font_weight='bold',
                arrows=True, arrowstyle='->', arrowsize=20)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        plt.show()

# Класс AVL-дерева (с балансировкой)
class AVLTree(BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, value):
            super().__init__(value)
            self.height = 1

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if node:
            node.height = max(self.get_height(node.left),
                             self.get_height(node.right)) + 1

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def rebalance(self, node):
        if not node:
            return node
        self.update_height(node)
        balance = self.get_balance(node)

        # LL
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        # LR
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # RR
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        # RL
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return self.Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node
        self.update_height(node)
        return self.rebalance(node)

    def visualize_with_matplotlib(self, title="AVL-дерево", figsize=(12, 8)):
        super().visualize_with_matplotlib(title=title, figsize=figsize)


# Демонстрация: несбалансированное (случайное) vs сбалансированное дерево
if __name__ == "__main__":
    # Элементы для вставки
    elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    print("Элементы для вставки:", elements)

    # Перемешиваем элементы для случайной вставки в несбалансированное дерево
    random.shuffle(elements)
    print("Порядок вставки в несбалансированное дерево:", elements)

    # Шаг 1: Создаём несбалансированное бинарное дерево со случайной логикой вставки
    bst = BinarySearchTree()
    for elem in elements:
        bst.insert(elem)
    print("\n--- НЕСБАЛАНСИРОВАННОЕ ДЕРЕВО (случайная вставка) ---")
    bst.visualize_with_matplotlib(title="Несбалансированное бинарное дерево (случайная структура)")

    # Шаг 2: Создаём сбалансированное AVL-дерево — вставляем те же элементы в исходном порядке
    avl = AVLTree()
    # Восстанавливаем исходный порядок элементов
    original_elements = sorted(elements)  # или исходный список, если важен порядок
    for elem in original_elements:
        avl.insert(elem)
    print("\n--- СБАЛАНСИРОВАННОЕ ДЕРЕВО (AVL-дерево) ---")
    avl.visualize_with_matplotlib(title="Сбалансированное AVL-дерево")
