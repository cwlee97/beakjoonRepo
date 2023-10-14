test_cases = int(input())
answer = test_cases
numbers = map(int, input().split(" "))
for number in numbers:
    if number == 1 or  number == 4:
        answer -= 1
        continue
    if number % 2 == 1 and number % (number//2)+1 == 0:
        answer -= 1
        continue
    for i in range(1, (number//2)-1):
            if number % (1+i) == 0 or number % (number-i) == 0:
                answer -= 1
                break
print(answer)