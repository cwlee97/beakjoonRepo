import sys

input = sys.stdin.readline

def getInput():
    nodes = int(input())
    graph = [[float("inf") for _ in range(nodes+1)]for _ in range(nodes+1)]

    for i in range(1, nodes+1):
        graph[i][i] = 0;

    while True:
        input_string = input()
        
        x, y = map(int, input_string.split(" "))

        if x == -1 and y == -1:
            break

        graph[x][y] = 1
        graph[y][x] = 1

    return nodes, graph

def solution(nodes, graph):
    distance_list = list()
    for k in range(1, nodes+1):
        for i in range(1, nodes+1):
            for j in range(1, nodes+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    distance_list = [max(graph[i][1:]) for i in range(1, nodes+1)]
    
    min_distance = min(distance_list)
    print(min_distance, distance_list.count(min_distance))
    for idx in range(len(distance_list)):
        if distance_list[idx] == min_distance:
            print(idx+1, end=" ")

if __name__ == "__main__":
    nodes, graph = getInput()
    solution(nodes, graph)
