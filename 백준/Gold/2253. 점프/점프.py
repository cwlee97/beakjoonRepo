import sys

input = sys.stdin.readline

def get_input():
    num_of_stones, num_of_small_stones = map(int, input().split(" "))
    small_stone_set = set()
    for _ in range(num_of_small_stones):
        small_stone = int(input())
        small_stone_set.add(small_stone)
    
    return num_of_stones, small_stone_set

def make_matrix(num_of_stones):
    # matrix : num_of_stones, velocity
    dp_list = [[10001 for _ in range(int((2*num_of_stones+1)**0.5)+2)] for _ in range(num_of_stones+1)]
    dp_list[1][0] = 0

    return dp_list

def solution(dp_list, num_of_stones, small_stone_set):
    for row in range(2, num_of_stones+1):
        if row not in small_stone_set:
            for col in range(1, int((2*num_of_stones+1)**0.5)+1):
                    next_value = min(dp_list[row-col][col-1], dp_list[row-col][col], dp_list[row-col][col+1]) + 1
                    dp_list[row][col] = next_value
    
    return dp_list

if __name__ == "__main__":
    num_of_stones, small_stone_set = get_input()
    dp_list = make_matrix(num_of_stones)
    dp_list = solution(dp_list, num_of_stones, small_stone_set)
    
    result = min(dp_list[-1])

    if result >= 10001:
        print(-1)
    else:
        print(result)