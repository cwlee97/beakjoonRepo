import sys

input = sys.stdin.readline

box_count = int(input())
box_array = list(map(int, input().split(" ")))
dp_array = [1 for _ in range(box_count)]

for i in range(box_count):
    for j in range(i+1, box_count):
        if box_array[i] < box_array[j]:
            dp_array[j] = max(dp_array[j], dp_array[i]+1)

print(max(dp_array))