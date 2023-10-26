import sys
from collections import deque
import copy

input = sys.stdin.readline

def BFS(graph, visited, row, col):
    queue = deque([(row, col)])
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    num_of_homes = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited[node[0]][node[1]] = True
            num_of_homes += 1

            for i in range(4):
                next_x = node[0] + dx[i]
                next_y = node[1] + dy[i]

                if 0<=next_x<len(graph) and 0<=next_y<len(graph) and visited[next_x][next_y] == False:
                    if graph[next_x][next_y] == 1:
                        queue.append((next_x, next_y))

        queue = deque(set(queue))
    return num_of_homes

if __name__ == "__main__":
    length = int(input())
    graph = list()
    homes = list()
    visited = [[False for _ in range(length)] for _ in range(length)]
    home_sets = 0

    for _ in range(length):
        graph.append(list(map(int, input().rstrip())))

    while True:
        before_homes = copy.copy(homes)

        for row in range(length):
            for col in range(length):
                if graph[row][col] != 0 and not visited[row][col]:
                    home_sets += 1
                    homes.append(BFS(graph, visited, row, col))

        if before_homes == homes:
            homes.sort()
            print(home_sets)
            for home in homes:
                print(home)
            break