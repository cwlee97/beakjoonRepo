import sys

input = sys.stdin.readline

def solution():
    cases = int(input())
    dp = list()

    for _ in range(cases):
        temp_list = list()
        if len(dp) == 0:
            dp.append(int(input()))
            continue
    
        input_list = list(map(int, input().split(" ")))

        for i in range(len(input_list)):
            if i == 0:
                temp_list.append(dp[0] + input_list[0])
            elif i == len(input_list)-1:
                temp_list.append(dp[-1] + input_list[-1])
            else:
                temp_list.append(max(dp[i-1], dp[i]) + input_list[i])
        dp = temp_list
    
    print(max(dp))
            

if __name__ == "__main__":
    solution()