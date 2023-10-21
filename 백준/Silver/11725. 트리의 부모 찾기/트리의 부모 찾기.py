import sys

input = sys.stdin.readline

def DFS(graph, root, parent):
    visited = {}
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.setdefault(node)
            stack += graph[node]
            for child in graph[node]:
                if child not in visited:
                    parent[child] = node

if __name__ == "__main__":
    node_count = int(input())
    parent = {i:i for i in range(2, node_count+1)}
    graph = {i:list() for i in range(1, node_count+1)}
    root = 1

    for _ in range(node_count-1):
        node1, node2 = map(int, input().split(" "))
        graph[node1].append(node2)
        graph[node2].append(node1)

    for key in graph.keys():
        graph[key].sort(reverse=True)

    DFS(graph, root, parent)
    
    for value in parent.values():
        print(value)