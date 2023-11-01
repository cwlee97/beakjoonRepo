import sys

input = sys.stdin.readline

def solution(num):
    if num == 1:
        print(1)
        return
    elif num == 2:
        print(2)
        return
    elif num == 3:
        print(4)
        return
    
    dp_arr = [0 for _ in range(num+1)]
    dp_arr[1] = 1
    dp_arr[2] = 2
    dp_arr[3] = 4

    for i in range(4, num+1):
        dp_arr[i] = dp_arr[i-3] + dp_arr[i-2] + dp_arr[i-1]

    print(dp_arr[-1])


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        solution(int(input()))