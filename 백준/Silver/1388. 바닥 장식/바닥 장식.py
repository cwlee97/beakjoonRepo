import sys

input = sys.stdin.readline

if __name__ == "__main__":
    rows, cols = map(int, input().split(" "))
    graph = list()
    for _ in range(rows):
        graph.append(list(input().rstrip()))

    answer = 0

    for row in range(rows):
        temp_char = ''
        for col in range(cols):
            if col == 0:
                temp_char = graph[row][col]
            if graph[row][col] != temp_char and graph[row][col] == '|':
                answer += 1
            elif col == cols-1 and graph[row][col] == '-':
                answer += 1
            temp_char = graph[row][col]
    for col in range(cols):
        for row in range(rows):
            if row == 0:
                temp_char = graph[row][col]
            if graph[row][col] != temp_char and graph[row][col] == '-':
                answer += 1
            elif row == rows-1 and graph[row][col] == '|':
                answer += 1
            temp_char = graph[row][col]
    print(answer)