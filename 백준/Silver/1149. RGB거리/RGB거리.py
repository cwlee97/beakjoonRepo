import sys

input = sys.stdin.readline

def get_input():
    num_of_homes = int(input())
    RGB_list = [None]

    for _ in range(num_of_homes):
        RGB_list.append(list(map(int, input().split(" "))))
         
    return num_of_homes, RGB_list

def solution(num_of_homes, RGB_list):
    dp_list = [[0 for _ in range(3)] for _ in range(num_of_homes+1)]

    dp_list[1] = RGB_list[1]

    for i in range(2, num_of_homes+1):
        for j in range(3):
            value_list = [dp_list[i-1][0], dp_list[i-1][1], dp_list[i-1][2]]
            del(value_list[j])
            dp_list[i][j] = min(value_list) + RGB_list[i][j]
    print(min(dp_list[-1]))

if __name__ == "__main__":
    num_of_homes, RGB_list = get_input()
    solution(num_of_homes, RGB_list)