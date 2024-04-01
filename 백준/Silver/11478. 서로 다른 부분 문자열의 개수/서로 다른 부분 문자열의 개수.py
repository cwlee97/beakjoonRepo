import sys

input = sys.stdin.readline

def getInput():
    input_str = input().rstrip()
    return input_str

def solution(input_str):
    res_set = set()
    for i in range(len(input_str)):
        for j in range(i, len(input_str)):
            sub_str = input_str[i:j+1]
            res_set.add(sub_str)

    print(len(res_set))

if __name__ == "__main__":
    input_str = getInput()
    solution(input_str)