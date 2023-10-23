import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def BFS(graph, queue, step, visited):
    next_queue = deque()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node == [len(graph)-1, len(graph[0])-1]:
                return step
            
            if len(graph)-1 > node[0] and graph[node[0]+1][node[1]] == '1':
                next_queue.append([node[0]+1, node[1]])
            if 0 < node[0] and graph[node[0]-1][node[1]] == '1':
                next_queue.append([node[0]-1, node[1]])
            if len(graph[0])-1 > node[1] and graph[node[0]][node[1]+1] == '1':
                next_queue.append([node[0], node[1]+1])
            if 0 < node[1] and graph[node[0]][node[1]-1] == '1':
                next_queue.append([node[0], node[1]-1])

    step += 1
    step = BFS(graph, next_queue, step, visited)
    return step

if __name__ == "__main__":
    rows, cols = map(int, input().split(" "))
    graph = list()
    
    for _ in range(rows):
        graph.append(input().rstrip())
    visited = list()
    start = [0, 0]
    queue = deque([start])
    step = 1
    step = BFS(graph, queue, step, visited)
    print(step)