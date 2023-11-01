import sys

input = sys.stdin.readline

count_of_num, cases = map(int, input().split(" "))

num_list = list(map(int, input().split(" ")))

dp_arr = [[None for _ in range(count_of_num+1)]]

dp_arr = [0] + num_list

for i in range(2, count_of_num+1):
    dp_arr[i] = dp_arr[i-1] + dp_arr[i]

for _ in range(cases):
    start, end = map(int, input().split(" "))
    print(dp_arr[end] - dp_arr[start-1])