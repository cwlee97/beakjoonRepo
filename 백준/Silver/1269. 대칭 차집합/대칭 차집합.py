import sys

input = sys.stdin.readline

def get_input():
    size_a, size_b = map(int, input().split(" "))
    set_a = list(map(int, input().split(" ")))
    set_b = list(map(int, input().split(" ")))

    return set_a, set_b

def solution(a, b):
    res = 0;
    res += len(set(a) ^ set(b))
    print(res);


if __name__ == "__main__":
    set_a, set_b = get_input()
    solution(set_a, set_b)