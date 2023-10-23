import sys
from collections import deque

input = sys.stdin.readline

def DFS(graph, vertex_info, root, visited_outside):
    visited = dict()
    queue = deque([root])
    connected_node_list = list()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.setdefault(node)
            if vertex_info[node-1] == '0':
                visited_outside.add(node)
                connected_node_list += graph[(node, vertex_info[node-1])]
                queue += graph[(node, vertex_info[node-1])]
    
    count_inside = len(set(connected_node_list) - visited_outside)

    return count_inside, visited_outside

if __name__ == "__main__":
    vertex_count = int(input())
    vertex_info = input()
    graph = {(i, vertex_info[i-1]): list() for i in range(1, vertex_count+1)}
    answer = 0
    visited_outside = set()
    for _ in range(vertex_count-1):
        vertex1, vertex2 = map(int, input().split(" "))
        graph[vertex1, vertex_info[vertex1-1]].append(vertex2)
        graph[vertex2, vertex_info[vertex2-1]].append(vertex1)
        if vertex_info[vertex1-1] == '1' and vertex_info[vertex2-1] == '1':
            answer += 2

    for i in range(1, vertex_count): # 마지막 node는 탐색 X
        if i not in visited_outside and vertex_info[i-1] == '0':
            root = i
            count_inside, visited_outside = DFS(graph, vertex_info, root, visited_outside)
            answer += count_inside*(count_inside-1)
    print(answer)