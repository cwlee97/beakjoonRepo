import sys
from collections import deque

input = sys.stdin.readline

def DFS(graph, vertex_info, root):
    visited = dict()
    queue = deque([root])
    count_inside = 0
    count_path = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.setdefault(node)
            if vertex_info[node-1] == '1':  # 방문 노드가 실내일 때
                count_inside += 1   # 실내 방문 횟수 1 증가
                if count_inside == 2:   # 실내 방문 횟수가 2이면
                    count_inside = 1
                    count_path += 1 # 경로갯수에 1 추가
                else:
                    queue += graph[node, vertex_info[node-1]]   # 실내 방문 횟수가 1이면 queue에 다음 탐색 노드 추가
            elif vertex_info[node-1] == '0': # 방문 노드가 실외이면
                if count_inside == 1:
                    visited.setdefault(node)
                    queue += graph[node, vertex_info[node-1]] 
    return count_path

if __name__ == "__main__":
    vertex_count = int(input())
    vertex_info = input()
    graph = {(i, vertex_info[i-1]): list() for i in range(1, vertex_count+1)}
    answer = 0
    for _ in range(vertex_count-1):
        vertex1, vertex2 = map(int, input().split(" "))
        graph[vertex1, vertex_info[vertex1-1]].append(vertex2)
        graph[vertex2, vertex_info[vertex2-1]].append(vertex1)

    for i in range(1, vertex_count+1):
        root = i
        answer += DFS(graph, vertex_info, root)
    print(answer)