import sys

input = sys.stdin.readline

def solution():
    k = int(input())

    binary_k = bin(k)[2:] 
    k_bits = len(binary_k)
    k_index = binary_k.rfind('1')


    next_power = 1 << k_bits
    if k == (next_power >> 1):
        next_power = k
        print(next_power, 0)
        return 0
    
    print(next_power, k_index+1)



if __name__ == "__main__":
    solution()