import sys

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    else:
                        current = current.right

    def post_order(self):
        if self.root:
            stack1 = []
            stack2 = []

            stack1.append(self.root)
            while stack1:
                node = stack1.pop()
                stack2.append(node)

                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)

            while stack2:
                node = stack2.pop()
                print(node.value)

if __name__ == "__main__":
    bst = BinarySearchTree()
    for line in sys.stdin:
        try:
            value = int(line)
            bst.insert(value)
        except ValueError:
            print("Invalid input:", line)

    bst.post_order()
