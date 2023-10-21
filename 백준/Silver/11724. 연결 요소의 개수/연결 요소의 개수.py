import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, root, vertex_count, answer, visited):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += set(graph_dict[node]) - set(visited)
        if not queue:
            answer += 1
    if len(visited) != vertex_count:
        for i in range(1, vertex_count+1):
            if i not in visited:
                root = i
                break
        answer = BFS(graph, root, vertex_count, answer, visited)
    return answer


if __name__ == "__main__":
    vertex_count, edge_count = map(int, input().split(" "))
    graph_dict = {i:list() for i in range(1, vertex_count+1)}
    answer = 0
    visited = list()
    root = 1

    for _ in range(edge_count):
        vertex1, vertex2 = map(int, input().split(" "))
        graph_dict[vertex1].append(vertex2)
        graph_dict[vertex2].append(vertex1)
    print(BFS(graph_dict, root, vertex_count, answer, visited))