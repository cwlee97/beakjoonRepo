import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    input_list = list()
    
    cases = int(input())

    for _ in range(cases):
        input_list.append(int(input()))

    heapq.heapify(input_list)

    while input_list:
        print(heapq.heappop(input_list))