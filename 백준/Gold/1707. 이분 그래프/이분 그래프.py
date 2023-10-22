from collections import deque
import sys

input = sys.stdin.readline

def BFS(graph, root, vertex_count):
    union = [0 for _ in range(vertex_count)]
    queue = deque([root-1])
    union[root-1] = 1
   
    while queue:
        node = queue.popleft()

        if node in graph[node]:
            return "NO"
        
        for vertex in graph[node]:
            if union[vertex] == 0:
                union[vertex] = union[node] * -1
                queue.append(vertex)
            elif union[node] == union[vertex]:
                return "NO"
            
        if not queue and union.count(0) != 0:
            new_root = union.index(0)
            queue.append(new_root)
            union[new_root] = 1
    return "YES"

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        vertex_count, edge_count = map(int, input().split(" "))
        graph = [list() for _ in range(vertex_count)]
        root = 1
        for _ in range(edge_count):
            vertex1, vertex2 = map(int, input().split(" "))
            graph[vertex1-1].append(vertex2-1)
            graph[vertex2-1].append(vertex1-1)
        print(BFS(graph, root, vertex_count))