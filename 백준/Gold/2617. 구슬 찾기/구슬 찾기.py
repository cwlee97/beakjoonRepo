import sys

input = sys.stdin.readline

def DFS(graph, root):
    stack = [root]
    visited = dict()
    count = -1

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.setdefault(node)
            count += 1
            stack += graph[node]
    return count

if __name__ == "__main__":
    vertexes, edges = map(int, input().split(" "))
    increase_graph = {i:list() for i in range(1, vertexes+1)}
    decrease_graph = {i:list() for i in range(1, vertexes+1)}
    result = [0 for _ in range(vertexes)]
    answer = 0

    for _ in range(edges):
        vertex1, vertex2 = map(int, input().split(" "))
        increase_graph[vertex1].append(vertex2)
        decrease_graph[vertex2].append(vertex1)
    
    for i in range(vertexes):
        if DFS(increase_graph, i+1) >= (vertexes+1)/2:
            answer += 1
        elif DFS(decrease_graph, i+1) >= (vertexes+1)/2:
            answer += 1
    
    print(answer)