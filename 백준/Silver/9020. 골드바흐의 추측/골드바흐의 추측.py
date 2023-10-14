import math

test_cases = int(input())
answer = test_cases
for i in range(test_cases):
    input_num = int(input())
    prime_list = list()
    for number in range(input_num // 2, 1, -1):
        status_a = True
        for i in range((int(math.sqrt(number))), 1, -1):
            if number % i == 0:
                status_a = False
                break
        if status_a == True:
            status_b = True
            temp_num = input_num - number
            for i in range((int(math.sqrt(temp_num))), 1, -1):
                if temp_num % i == 0:
                    status_b = False
                    break
            if status_b == True:
                print("{} {}".format(number, temp_num))
                break