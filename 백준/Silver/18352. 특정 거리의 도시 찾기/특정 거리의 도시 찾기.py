import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(graph, visited, distance, queue, count):
    new_queue = deque()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.setdefault(node)
            distance[node-1] += count
            new_queue += graph[node]
    if len(new_queue) == 0:
        return distance
    count += 1
    distance = solution(graph, visited, distance, new_queue, count)

    return distance

if __name__ == "__main__":
    cities, roads, road_info, start_city = map(int, input().split(" "))
    graph = {i:list() for i in range(1, cities+1)}
    visited = dict()
    count = 0
    distance = [0 for _ in range(cities)]
    queue = deque([start_city])

    for _ in range(roads):
        city1, city2 = map(int, input().split(" "))
        graph[city1].append(city2)

    distance = solution(graph, visited, distance, queue, count)

    if distance.count(road_info) == 0:
        print(-1)
    else:
        for i in range(len(distance)):
            if distance[i] == road_info:
                print(i+1)