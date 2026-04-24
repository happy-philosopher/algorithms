# Напишите функцию для обхода бинарного дерева в ширину (Breadth-First Search, BFS).


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_traversal(root):
    """
    Обход бинарного дерева в ширину (Breadth-First Search).
    Args:
        root: корень бинарного дерева (объект TreeNode или None)
    Returns:
        list: список значений узлов в порядке обхода BFS
    """
    if not root:
        return []

    result = []
    queue = deque([root])  # Используем очередь для BFS

    while queue:
        # Извлекаем узел из начала очереди
        current_node = queue.popleft()
        result.append(current_node.val)

        # Добавляем дочерние узлы в конец очереди (если существуют)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


# Создаём дерево:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Выполняем обход
result = bfs_traversal(root)
print(result)
