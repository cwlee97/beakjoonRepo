import sys
from collections import deque

def BFS(graph, visited, count, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if  0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]) and not visited[next_x][next_y]:
                if graph[next_x][next_y] != 0:
                    visited[next_x][next_y] = True
                    queue.append([next_x, next_y])
                else:
                    count[current_x][current_y] += 1
    return 1

if __name__ == "__main__":
    rows, cols = map(int, input().split(" "))
    graph = list()
    for _ in range(rows):
        graph.append(list(map(int, input().split(" "))))
    year = 0

    while True:
        answer = list()
        visited = [[False] * cols for _ in range(rows)]
        count = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if graph[row][col] != 0 and not visited[row][col]:
                    answer.append(BFS(graph, visited, count, row, col))
        
        for row in range(rows):
            for col in range(cols):
                graph[row][col] -= count[row][col]
                if graph[row][col] < 0:
                    graph[row][col] = 0
        
        if len(answer) == 0 or len(answer) >= 2:
            break
        
        year += 1
    
    if len(answer) >= 2:
        print(year)
    else:
        print(0)