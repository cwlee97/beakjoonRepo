import sys

input = sys.stdin.readline
cases = int(input())

for _ in range(cases):
    arr_len = int(input())
    arr = list(map(int, input().split(" ")))

    arr.sort()

    min_level = arr[1]-arr[0]

    for i in range(arr_len-2):
        if arr[i+2]-arr[i] >  min_level:
            min_level =  arr[i+2]-arr[i]
        
    print(min_level)