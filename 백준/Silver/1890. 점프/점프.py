# 틀린 코드

import sys

input = sys.stdin.readline

def get_input():
    size = int(input())
    input_map = list()

    for _ in range(size):
        input_map.append(list(map(int, input().split(" "))))

    return size, input_map

def solution(size, input_map):
    dp = [0 for _ in range(size*size)]
    
    for i in range(len(dp)-1):
        if i == 0:
            if input_map[0][0] < size:
                dp[size*input_map[0][0]] += 1
                dp[input_map[0][0]] += 1
                continue

        if dp[i] != 0:
            if i//size + input_map[i//size][i%size] < size:
                dp[i + size*input_map[i//size][i%size]] += dp[i]

            if i%size + input_map[i//size][i%size] < size:
                dp[i + input_map[i//size][i%size]] += dp[i]
                
    print(dp[-1])

if __name__ == "__main__":
    size, input_map = get_input()
    solution(size, input_map)