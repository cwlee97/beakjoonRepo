import sys
from collections import deque

input = sys.stdin.readline

def knapsack(num_of_items, weight_limit, weight_and_price, array):

    for item in range(1, num_of_items+1):
        item_weight, item_price = weight_and_price.popleft()
        for weight in range(1, weight_limit+1):
            if weight < item_weight:
                array[item][weight] = array[item-1][weight]
            else:
                array[item][weight] = max(array[item-1][weight], array[item-1][weight-item_weight] + item_price)

    return array[-1][-1]

if __name__ == "__main__":

    num_of_items, weight_limit = map(int, input().split(" "))

    weight_and_price = list()

    for _ in range(num_of_items):
        weight_and_price.append(tuple(map(int, input().split(" "))))

    weight_and_price.sort(key=lambda x:x[0])
    weight_and_price = deque(weight_and_price)

    knapsack_array = [[0 for _ in range(weight_limit+1)] for _ in range(num_of_items+1)]

    print(knapsack(num_of_items, weight_limit, weight_and_price, knapsack_array))