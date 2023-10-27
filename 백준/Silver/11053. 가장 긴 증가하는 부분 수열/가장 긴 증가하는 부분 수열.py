import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    cases = int(input())
    num_queue = deque(list(map(int, input().split(" "))))

    result_list = list()

    while num_queue:
        num = num_queue.popleft()

        if len(result_list) == 0:
            result_list.append(num)
            continue
    
        if num > result_list[-1]:
            result_list.append(num)

        elif num < result_list[0]:
            result_list[0] = num
        
        else:
            for i in range(len(result_list)):
                if result_list[i-1]< num < result_list[i]:
                    result_list[i] = num
    print(len(result_list))
