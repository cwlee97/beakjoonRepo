import sys

input = sys.stdin.readline

if __name__ == "__main__":
    num_of_coin, total_price = map(int, input().split(" "))
    coin_list = list()
    answer = 0

    for _ in range(num_of_coin):
        coin_list.append(int(input()))
    
    while total_price > 0:
        coin = coin_list.pop()

        calc_result = total_price // coin

        if calc_result != 0:
            answer += calc_result
            total_price = total_price % coin
    print(answer)