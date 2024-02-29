import sys

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
    x, y = map(int, input().split(" "))
    denominator = 1
    numerator = 1
    for i in range(x):
        denominator *= i+1
    
    for j in range(x):
        numerator *= y-j

    res = numerator / denominator
    print(int(res))