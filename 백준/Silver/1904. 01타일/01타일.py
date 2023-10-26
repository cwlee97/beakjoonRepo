import sys
from collections import deque

input = sys.stdin.readline

def stair_dp(n, stair_array):
    count = 0

    if n == 1:
        return stair_array[0]
    
    elif n == 2:
        return stair_array[1]
    
    while count < n-2:
        calc_result = (stair_array[1] + stair_array[0]) % 15746
        stair_array.popleft()
        stair_array.append(calc_result)
        count += 1
    return calc_result

if __name__ == "__main__":
    length = int(input())
    stair_array = deque([1, 2])
    result = stair_dp(length, stair_array)
    print(result)