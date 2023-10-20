def preOrder(binary_tree, node_value):
    print(node_value, end="")
    if binary_tree[node_value][0] != ".":
        preOrder(binary_tree, binary_tree[node_value][0])
    if binary_tree[node_value][1] != ".":
        preOrder(binary_tree, binary_tree[node_value][1])

def inOrder(binary_tree, node_value):
    if binary_tree[node_value][0] != ".":
        inOrder(binary_tree, binary_tree[node_value][0])
    print(node_value, end="")
    if binary_tree[node_value][1] != ".":
        inOrder(binary_tree, binary_tree[node_value][1])

def postOrder(binary_tree, node_value):
    if binary_tree[node_value][0] != ".":
        postOrder(binary_tree, binary_tree[node_value][0])
    if binary_tree[node_value][1] != ".":
        postOrder(binary_tree, binary_tree[node_value][1])
    print(node_value, end="")


if __name__ == "__main__":
    total_test_case = int(input())
    binary_tree_dict = dict()
    for i in range(total_test_case):
        node_info = input().split(" ")
        binary_tree_dict[node_info[0]] = node_info[1:]
    preOrder(binary_tree_dict, 'A')
    print()
    inOrder(binary_tree_dict, 'A')
    print()
    postOrder(binary_tree_dict, 'A')