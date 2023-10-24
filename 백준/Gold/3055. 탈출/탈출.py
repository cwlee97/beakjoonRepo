import sys
from collections import deque
from itertools import chain
import copy

input = sys.stdin.readline

def check(queue, count):
    temp_queue=copy.copy(queue)
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while temp_queue:
        node = temp_queue.popleft()
        for i in range(4):
            next_x = node[0] + dx[i]
            next_y = node[1] + dy[i]
            if 0<=next_x<len(graph) and 0<=next_y<len(graph[0]):
                if graph[next_x][next_y] == 'D':
                    print(count)
                    exit(0)

def BFS_water(graph, water):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    next_water = deque()

    while water:
        water_node = water.pop()
        for i in range(4):
            next_x_water = water_node[0] + dx[i]
            next_y_water = water_node[1] + dy[i]

            if 0<=next_x_water<len(graph) and 0<=next_y_water<len(graph[0]):
                if graph[next_x_water][next_y_water] == '.' or graph[next_x_water][next_y_water] == 'S':
                    graph[next_x_water][next_y_water] = '*'
                    next_water.append([next_x_water, next_y_water])
    return graph, next_water

def BFS_s(graph, queue, count, end_node):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    next_queue = deque()
    while queue:
        node = queue.popleft()
        
        for i in range(4):
            next_x = node[0] + dx[i]
            next_y = node[1] + dy[i]
        
            if 0<=next_x<len(graph) and 0<=next_y<len(graph[0]):
                if graph[next_x][next_y] == '.':
                    graph[next_x][next_y] = 'S'
                    next_queue.append([next_x, next_y])
                if next_x == end_node[0] and next_y == end_node[1]:
                    print(count)
                    exit(0)
                    
    return graph, next_queue, count
if __name__ == "__main__":
    rows, cols = map(int, input().split(" "))
    graph = list()
    queue = deque()
    water = deque()
    count = 0

    for row in range(rows):
        temp_str = input().rstrip()
        graph.append(list(temp_str))

        for col in range(cols):
            if graph[row][col] == 'D':
                end_node=[row, col]
            elif graph[row][col] == 'S':
                queue.append([row, col])
                start_node= [row, col]
            elif graph[row][col] == '*':
                water.append([row, col])
    
    while count < rows*cols:
        count += 1
        check(queue, count)
        graph, water = BFS_water(graph, water)
        graph, queue, count = BFS_s(graph, queue, count, end_node)
        if 'S' not in list(chain(*graph)):
            print('KAKTUS')
            exit(0)
        if not queue:
            print('KAKTUS')
            exit(0)
    print("KAKTUS")