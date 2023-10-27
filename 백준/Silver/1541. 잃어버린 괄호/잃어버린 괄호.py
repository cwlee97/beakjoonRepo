import sys

if __name__ == "__main__":
    calc_str = input()
    temp_str = ""

    num_list, oper_list = list(), list()
    result = 0

    for char in calc_str:
        if char == '+' or char == '-':
            if temp_str != "":
                num_list.append(int(temp_str))
            oper_list.append(char)
            temp_str = ""
        else:
            temp_str += char
    num_list.append(int(temp_str))

    if oper_list.count('-') == 0:
        print(sum(num_list))
        exit(0)

    for i in range(1, len(oper_list)):
        if oper_list[i-1] == '-':
            oper_list[i] = '-'

    for i in range(len(num_list)):
        if i == 0:
            result += num_list[i]
            continue

        if oper_list[i-1] == '+':
            result += num_list[i]
        elif oper_list[i-1] == '-':
            result -= num_list[i]

    print(result)