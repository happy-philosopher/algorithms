# Напишите три функции для обхода бинарного дерева в глубину (Depth-First Search, DFS):
# прямой обход (preorder), симметричный обход (inorder) и обратный обход (postorder).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    """
    Прямой обход (Preorder): корень → левое поддерево → правое поддерево
    """
    result = []
    def dfs(node):
        if node:
            result.append(node.val)     # Посещаем текущий узел
            dfs(node.left)              # Обходим левое поддерево
            dfs(node.right)             # Обходим правое поддерево
    dfs(root)
    return result


def inorder_traversal(root):
    """
    Симметричный обход (Inorder): левое поддерево → корень → правое поддерево
    """
    result = []
    def dfs(node):
        if node:
            dfs(node.left)              # Обходим левое поддерево
            result.append(node.val)     # Посещаем текущий узел
            dfs(node.right)             # Обходим правое поддерево
    dfs(root)
    return result


def postorder_traversal(root):
    """
    Обратный обход (Postorder): левое поддерево → правое поддерево → корень
    """
    result = []
    def dfs(node):
        if node:
            dfs(node.left)              # Обходим левое поддерево
            dfs(node.right)             # Обходим правое поддерево
            result.append(node.val)     # Посещаем текущий узел
    dfs(root)
    return result


# Пример использования
if __name__ == "__main__":
    # Создаём бинарное дерево:
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

    # Выполняем все три вида обхода
    print("Preorder (прямой):", preorder_traversal(root))
    print("Inorder (симметричный):", inorder_traversal(root))
    print("Postorder (обратный):", postorder_traversal(root))
