import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def hanoi(n, start, mid, end, result_str):
    if n == 1:
        print("%s %s" %(start, end))
        return
    
    hanoi(n-1, start, end, mid ,result_str)

    print("%s %s" %(start, end))

    hanoi(n-1, mid, start, end, result_str)

    return

# 점화식
# f(n) = 2f(n-1) + 1
if __name__ == "__main__":
    n = int(input())

    if n <= 20:
        print(2**n-1)
        hanoi(n, 1, 2, 3, "")
    else:
        print(2**n-1)