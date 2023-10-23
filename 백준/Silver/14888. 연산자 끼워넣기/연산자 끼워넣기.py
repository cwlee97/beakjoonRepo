# 연산자 combination?
import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline

def calculator(numbers, operator_list):
    minimum = 1e9
    maximum = -1e9
    oper_comb = permutations(operator_list, len(operator_list))
    for operators in oper_comb:
        operators = list(operators)
        numbers_copy = numbers.copy()
        result = numbers_copy.popleft()
        while operators:
            operator = operators.pop()
            if operator == 0:
                result += numbers_copy.popleft()
            elif operator == 1:
                result -= numbers_copy.popleft()
            elif operator == 2:
                result *= numbers_copy.popleft()
            elif operator == 3:
                if result < 0:
                    result *= -1
                    result = result // numbers_copy.popleft()
                    result *= -1
                else:
                    result = result // numbers_copy.popleft()
        minimum = min(result, minimum)
        maximum = max(result, maximum)
    return minimum, maximum

if __name__ == "__main__":
    test_cases = int(input())
    numbers = deque(map(int, input().split(" ")))
    operators_count = list(map(int, input().split(" ")))
    operator_list = list()
    for i in range(len(operators_count)):
        for j in range(operators_count[i]):
            operator_list.append(i)
    
    minimum, maximum = calculator(numbers, operator_list)

    print("{}\n{}".format(maximum, minimum))