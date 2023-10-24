import sys
import heapq

input = sys.stdin.readline

def BFS(x, y, visited, graph):
    heap = []
    heapq.heappush(heap, (0, x, y))

    while heap:
        count, current_x, current_y = heapq.heappop(heap)
        visited[current_x][current_y] = True

        if current_x == size-1 and current_y == size-1:
            return count
        
        for i in range(4):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if (0<=next_x<size) and (0<=next_y<size) and not visited[next_x][next_y]:
                visited[next_x][next_y] = True

                if graph[next_x][next_y] == '1':
                    heapq.heappush(heap, (count, next_x, next_y))
                elif graph[next_x][next_y] == '0':
                    heapq.heappush(heap, (count+1, next_x, next_y))

if __name__ == "__main__":
    size = int(input())
    graph = list()
    for _ in range(size):
        graph.append(input())
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[False for _ in range(size)] for _ in range(size)]

    print(BFS(0, 0, visited, graph))