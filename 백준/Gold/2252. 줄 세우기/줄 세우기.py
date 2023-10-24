import sys
from collections import deque

input = sys.stdin.readline

def topologicalSort(graph, incoming_degree):
    visited = dict()
    result = deque()
    start_point = deque()

    for node in range(len(incoming_degree)):
        if incoming_degree[node] == 0:
            start_point.append(node)
    
    while len(result) < len(incoming_degree):
        current_node = start_point.popleft() + 1
        result.append(current_node)

        # node의 outgoing edge 제거
        for next_node in graph[current_node]:
            incoming_degree[next_node-1] -= 1
            if incoming_degree[next_node-1] == 0:
                start_point.append(next_node-1)
    return result



if __name__ == "__main__":
    vertex_count, edge_count = map(int, input().split(" "))
    graph = {i:list() for i in range(1, vertex_count+1)}
    incoming_degree = [0 for _ in range(vertex_count)]
    
    for _ in range(edge_count):
        vertex1, vertex2 = map(int, input().split(" "))
        graph[vertex1].append(vertex2)
        incoming_degree[vertex2-1] += 1
    
    result = topologicalSort(graph, incoming_degree)
    print(*result)