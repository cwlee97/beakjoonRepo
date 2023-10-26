import sys

input = sys.stdin.readline

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        num_of_coin = int(input())
        coin_list = list(map(int, input().split(" ")))
        total_price = int(input())

        result_list = [0 for _ in range(total_price+1)]

        result_list[0] = 1
        
        for coin in coin_list:
            for idx in range(coin, total_price+1):
                result_list[idx] += result_list[idx-coin]
        print(result_list[-1])