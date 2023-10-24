import sys
from collections import deque
import copy

input = sys.stdin.readline

def BFS(graph, ripe_tomato):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while ripe_tomato:
        x, y, z = ripe_tomato.popleft()

        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]
        
            if (0<=next_x<len(graph)) and (0<=next_y<len(graph[0])) and (0<=next_z<len(graph[0][0])):
                if graph[next_x][next_y][next_z] == 0:
                    graph[next_x][next_y][next_z] = graph[x][y][z] + 1
                    ripe_tomato.append([next_x, next_y, next_z])
    return graph

if __name__ == "__main__":
    cols, rows, boxes = map(int, input().split(" "))

    graph = list()
    box_list = list()
    ripe_tomato = deque()
    not_tomato = 0
    days = 0

    for row in range(rows*boxes):
        tomato_row = list(map(int, input().split(" ")))
        box_list.append(tomato_row)
        for col in range(cols):
            if tomato_row[col] == 1:
                ripe_tomato.append([row//rows,row%rows, col])
            elif tomato_row[col] == -1:
                not_tomato += 1
        if row % rows == rows-1:
            graph.append(box_list)
            box_list = list()
    graph = BFS(graph, ripe_tomato)
    for box in graph:
        for row in box:
            for ele in row:
                if ele == 0:
                    print(-1)
                    exit(0)
            days = max(days, max(row))
    print(days-1)