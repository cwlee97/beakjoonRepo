import sys

input = sys.stdin.readline

def solution():
    cases = int(input())

    result = 0
    plus_num_list = list()
    minus_num_list = list()

    for _ in range(cases):
        input_num = int(input())
        if input_num > 0:
            plus_num_list.append(input_num)
        else:
            minus_num_list.append(input_num)

    plus_num_list.sort(reverse=True)
    minus_num_list.sort()

    if len(plus_num_list)%2==1:
        result += plus_num_list.pop()
    if len(minus_num_list)%2==1:
        result += minus_num_list.pop()

    for i in range(1, len(plus_num_list), 2):
        result += max(plus_num_list[i]*plus_num_list[i-1], plus_num_list[i]+plus_num_list[i-1])
    for i in range(1, len(minus_num_list), 2):
        result += max(minus_num_list[i]*minus_num_list[i-1], minus_num_list[i]+minus_num_list[i-1])
    
    print(result)

if __name__ == "__main__":
    solution()