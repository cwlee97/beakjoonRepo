def func(a, b):
    times = int(a)
    string = b
    result = str()

    for char in string:
        result += char * times

    return result

test_cases = int(input())
for i in range(test_cases):
    times, string = input().split(" ")
    answer = func(times, string)
    print(answer)