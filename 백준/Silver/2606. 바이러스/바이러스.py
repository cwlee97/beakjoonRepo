import sys
from collections import deque

input = sys.stdin.readline

def BFS(graph, root):
    visited = list()
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += set(graph[node]) - set(visited)

    return len(visited)

if __name__ == "__main__":
    vertex_count = int(input())
    edge_count = int(input())
    graph_dict = {i:list() for i in range(1, vertex_count+1)}

    for _ in range(edge_count):
        vertex1, vertex2 = map(int, input().split(" "))
        graph_dict[vertex1].append(vertex2)
        graph_dict[vertex2].append(vertex1)

    root = 1

    print(BFS(graph_dict, root)-1)