# 실외를 기준으로 DFS탐색을 실시하면 시간초과로 풀이할 수 없었음
# 실내를 기준으로 탐색하는 코드 작성

import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def DFS1(graph, vertex_info, root, visited_outside):
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

def DFS2(graph, vertex_info, root):
    visited = dict()
    queue = deque([root])
    count_inside = 0
    count_path = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.setdefault(node)
            if vertex_info[node-1] == '1' and node >= root:  # 방문 노드가 실내일 때
                count_inside += 1   # 실내 방문 횟수 1 증가
                if count_inside == 2:   # 실내 방문 횟수가 2이면
                    count_inside = 1
                    count_path += 1 # 경로갯수에 1 추가
                else:
                    queue += graph[node, vertex_info[node-1]]   # 실내 방문 횟수가 1이면 queue에 다음 탐색 노드 추가
            elif vertex_info[node-1] == '0': # 방문 노드가 실외이면
                if count_inside == 1:
                    queue += graph[node, vertex_info[node-1]]
    return count_path

if __name__ == "__main__":
    vertex_count = int(input())
    vertex_info = input()
    graph = {(i, vertex_info[i-1]): list() for i in range(1, vertex_count+1)}
    answer1 = 0
    answer2 = 0
    visited_outside = set()
    for _ in range(vertex_count-1):
        vertex1, vertex2 = map(int, input().split(" "))
        graph[vertex1, vertex_info[vertex1-1]].append(vertex2)
        graph[vertex2, vertex_info[vertex2-1]].append(vertex1)
        if vertex_info[vertex1-1] == '1' and vertex_info[vertex2-1] == '1':
            answer1 += 2

    if vertex_count > 1000:
        for i in range(1, vertex_count): # 마지막 node는 탐색 X
            if i not in visited_outside and vertex_info[i-1] == '0':
                root = i
                count_inside, visited_outside = DFS1(graph, vertex_info, root, visited_outside)
                answer1 += count_inside*(count_inside-1)
        print(answer1)
    else:
        for i in range(1, vertex_count): # 마지막 node는 탐색 X
            if vertex_info[i-1] == '1':
                root = i
                answer2 += DFS2(graph, vertex_info, root)
        print(answer2*2)