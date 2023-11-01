import sys

input = sys.stdin.readline

def get_input():
    num_of_stairs = int(input())
    stair_weight_list = [None]

    for _ in range(num_of_stairs):
        stair_weight_list.append(int(input()))
    
    return num_of_stairs, stair_weight_list

def solution(num_of_stairs, stair_weight_list):

    if num_of_stairs == 1:
        print(stair_weight_list[1])
        return

    if num_of_stairs == 2:
        print(stair_weight_list[1] + stair_weight_list[2])
        return

    dp_list = [0 for _ in range(num_of_stairs+1)]
    dp_list[1] = stair_weight_list[1]
    dp_list[2] = stair_weight_list[1] + stair_weight_list[2]
    
    for i in range(3, num_of_stairs+1):
        dp_list[i] = max(dp_list[i-2], dp_list[i-3] + stair_weight_list[i-1])+ stair_weight_list[i]
    print(dp_list[-1])
    return

if __name__ == "__main__":
    num_of_stairs, stair_weight_list = get_input()
    solution(num_of_stairs, stair_weight_list)