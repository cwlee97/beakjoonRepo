import sys
import heapq

input = sys.stdin.readline
inf = int(1e9)

def dijkstra(graph, distances, node):
    queue = []
    heapq.heappush(queue, (0, start_city))

    while queue:
        dist, node = heapq.heappop(queue)
        if distances[node-1] < dist:
            continue
        for next_node in graph[node]:
            weight = distances[node-1] + next_node[1]
            if weight < distances[next_node[0]-1]:
                distances[next_node[0]-1] = weight
                heapq.heappush(queue, (weight, next_node[0]))

    return distances

if __name__ == "__main__":
    cities = int(input())
    buses = int(input())
    distances = [1e9 for _ in range(cities)]
    graph = {i:list() for i in range(1, cities+1)}
    visited = dict()

    for _ in range(buses):
        start, end, weight = map(int, input().split(" "))
        graph[start].append((end, weight))
    
    start_city, end_city = map(int, input().split(" "))
    distances[start_city-1] = 0

    distances = dijkstra(graph, distances, start_city)

    print(distances[end_city-1])