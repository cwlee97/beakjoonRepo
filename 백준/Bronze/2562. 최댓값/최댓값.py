arr = list()
for i in range(1, 9 + 1):
    arr.append(int(input()))
sorted_arr = sorted(arr, reverse=True)
first_answer = sorted_arr[0]
second_answer = arr.index(first_answer) + 1
print(first_answer)
print(second_answer)