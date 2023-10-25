import sys
import heapq
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    total_parts = int(input())
    edges = int(input())
    graph = {i:dict() for i in range(1, total_parts+1)}
    result = {i:0 for i in range(1, total_parts+1)}
    incoming_degree = [0 for _ in range(total_parts)]

    for _ in range(edges):
        mother_part, child_part, count = map(int, input().split(" "))
        graph[mother_part][child_part] = count
        incoming_degree[child_part-1] += 1
    collections = deque([total_parts])
    while collections:
        node = collections.popleft()
        incoming_degree[node-1] -= 1

        used = False
        for key, value in graph[node].items():
            incoming_degree[key-1] -= 1
            if result[node] == 0:
                result[key] += value
            else:
                used = True
                result[key] += result[node] * value
        if used == True:
            result[node] = 0
        for next_node in range(total_parts):
            if incoming_degree[next_node] == 0:
                collections.append(next_node+1)
                break
    for key, value in result.items():
        if value != 0:
            print("{} {}".format(key, value))