import sys
from collections import deque

input = sys.stdin.readline

def BFS(graph_dict, root):
    visited = {}
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.setdefault(node)
            queue += graph_dict[node]
    return visited

def DFS(graph_dict, root):
    visited = {}
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.setdefault(node)
            stack += reversed(graph_dict[node])
    return visited

if __name__ == "__main__":
    vertex_count, edge_count, root = map(int, input().split(" "))
    graph_dict = {i:list() for i in range(1, vertex_count+1)}
    for _ in range(edge_count):
        vertex1, vertex2 = map(int, input().split(" "))
        graph_dict[vertex1].append(vertex2)
        graph_dict[vertex2].append(vertex1)
    for key in graph_dict:
        graph_dict[key].sort()
    print(*DFS(graph_dict, root))
    print(*BFS(graph_dict, root))