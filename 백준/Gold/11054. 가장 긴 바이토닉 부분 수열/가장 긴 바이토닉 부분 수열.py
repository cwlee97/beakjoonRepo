import sys

input = sys.stdin.readline

def get_input():
    cases = int(input())
    num_list = list(map(int, input().split(" ")))
    return cases, num_list

def solution(cases, num_list):
    # 1번 순회로 풀리는 이전 문제와는 다르게 풀어야할듯
    # 원소마다 바이토닉 부분수열을 만들면서 최장길이를 갱신하는 방식?

    max_length = 0

    for i in range(len(num_list)):
        before_num_list = num_list[:i+1]
        after_num_list = num_list[i:]
        before_sub_list = list()
        after_sub_list = list()

        for num in before_num_list:
            if len(before_sub_list) == 0:
                before_sub_list.append(num)
                continue
            if num > before_sub_list[-1]:
                before_sub_list.append(num)
            elif num < before_sub_list[0]:
                before_sub_list[0] = num
            else:
                for j in range(1, len(before_sub_list)):
                    if before_sub_list[j-1]<num and num<before_sub_list[j]:
                        before_sub_list[j] = num
                        break

        for num in after_num_list:
            if len(after_sub_list) == 0:
                after_sub_list.append(num)
                continue
            if num < after_sub_list[-1]:
                after_sub_list.append(num)
            elif num > after_sub_list[0]:
                after_sub_list[0] = num
            else:
                for j in range(1, len(after_sub_list)):
                    if after_sub_list[j]<num<after_sub_list[j-1]:
                        after_sub_list[j] = num
                        break

        max_length = max(max_length, len(before_sub_list)+len(after_sub_list)-1)

    print(max_length)

if __name__ == "__main__":
    cases, num_list = get_input()
    solution(cases, num_list)