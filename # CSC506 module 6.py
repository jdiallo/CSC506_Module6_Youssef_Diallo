# CSC506 module 6 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.data < other.data

class Tree:
    def __init__(self, data_array):
        self.root = self.build_tree(data_array)

    def build_tree(self, data_array):
        sorted_data = sorted(set(data_array))  # Sort and remove duplicates
        return self._build_tree_helper(sorted_data)

    def _build_tree_helper(self, data_array):
        if not data_array:
            return None

        mid = len(data_array) // 2
        root = Node(data_array[mid])
        root.left = self._build_tree_helper(data_array[:mid])
        root.right = self._build_tree_helper(data_array[mid+1:])
        return root

    def insert(self, value):
        self.root = self._insert_helper(self.root, value)

    def _insert_helper(self, node, value):
        if not node:
            return Node(value)

        if value < node.data:
            node.left = self._insert_helper(node.left, value)
        else:
            node.right = self._insert_helper(node.right, value)
        return node

    def delete(self, value):
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(self, node, value):
        if not node:
            return None

        if value < node.data:
            node.left = self._delete_helper(node.left, value)
        elif value > node.data:
            node.right = self._delete_helper(node.right, value)
        else:
            # Node with one or no children
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children
            successor = self._find_min_value_node(node.right)
            node.data = successor.data
            node.right = self._delete_helper(node.right, successor.data)

        return node

    def _find_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Example usage
data_array = [8, 3, 10, 1, 6, 14, 4, 7, 13]
tree = Tree(data_array)

# Visual representation (using ASCII tree)
def print_tree(node):
    if not node:
        return
    print(node.data)
    print_tree(node.left)
    print_tree(node.right)

print_tree(tree.root)

# Insert and delete operations
tree.insert(11)
print_tree(tree.root)
tree.delete(8)
print_tree(tree.root)
