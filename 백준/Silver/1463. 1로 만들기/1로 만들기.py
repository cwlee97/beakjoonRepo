import sys

input = sys.stdin.readline

def calc(num, dp):
    if num == 1:
        print(0)
        return
    elif num <= 3:
        print(1)
        return
    
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, num+1):
        if i % 3 == 0:
            val1 = dp[i//3] + 1
        else:
            val1 = dp[i-i%3] + (i%3)

        if i % 2 == 0:
            val2 = dp[i//2] + 1
        else:
            val2 = dp[i-1] + 1

        dp[i] = min(val1, val2)

    print(dp[-1])
         
if __name__ == "__main__":
    input_num = int(input())
    dp = [0 for _ in range(input_num+1)]
    calc(input_num, dp)