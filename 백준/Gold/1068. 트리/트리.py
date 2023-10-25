import sys
from collections import deque

input = sys.stdin.readline

def DFS(graph, root, node, remove_node, visited, result):
    visited[node] = True
    if len(graph[node]) == 0:
        if node == root:
            return 0
        else:
            result += 1
    elif len(graph[node]) == 1 and graph[node][0] == remove_node:
        result += 1
    for next_node in graph[node]:
        if not visited[next_node] and next_node != remove_node:
            result = DFS(graph, root, next_node, remove_node, visited, result)
    return result


if __name__ == "__main__":
    nodes = int(input())
    graph = {i:list() for i in range(nodes)}
    visited = [False for _ in range(nodes)]
    result = 0

    node_info = list(map(int, input().split(" ")))
    
    remove_node = int(input())
    
    for i in range(nodes):
        if node_info[i] == -1:
            root = i
            continue
        graph[node_info[i]].append(i)

    graph[remove_node] = list()
    
    print(DFS(graph, root, root, remove_node, visited, result))