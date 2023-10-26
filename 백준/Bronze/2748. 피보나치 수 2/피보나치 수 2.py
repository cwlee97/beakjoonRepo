import sys

input = sys.stdin.readline

def fibo(n, fibo_array):
    if 0<n<= 2:
        fibo_array[n] = 1
    if fibo_array[n] != 0:
        return fibo_array[n]
    fibo_array[n] = fibo(n-1, fibo_array) + fibo(n-2, fibo_array)
    return fibo_array[n]

if __name__ == "__main__":
    input_number = int(input())
    fibo_array = [0 for _ in range(input_number+1)]
    print(fibo(input_number, fibo_array))