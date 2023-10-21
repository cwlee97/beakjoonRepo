import sys

input = sys.stdin.readline

def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return x

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    vertex_count, edge_count = map(int, input().split(" "))
    graph_info_list = list()
    total_weight = 0
    total_path = 0
    visited = list()

    for _ in range(edge_count):
        vertex1, vertex2, weight = map(int, input().split(" "))
        graph_info_list.append([weight, vertex1, vertex2])
    graph_info_list.sort(key=lambda x: x[0])

    parent = {i:i for i in range(1, vertex_count+1)}

    for graph_info in graph_info_list:
        if find(graph_info[1], parent) != find(graph_info[2], parent):
            union(graph_info[1], graph_info[2], parent)
            total_weight += graph_info[0]
            total_path += 1
        if total_path == vertex_count-1:
            print(total_weight)
            break