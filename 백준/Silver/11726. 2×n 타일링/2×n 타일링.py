import sys

input = sys.stdin.readline

def solution(width):
    if width == 1:
        print(1)
        return
    
    elif width == 2:
        print(2)
        return
    
    dp_list = [0 for _ in range(width+1)]
    dp_list[1] = 1
    dp_list[2] = 2
    
    for i in range(3, width+1):
        dp_list[i] = ((dp_list[i-2] % 10007) + (dp_list[i-1] % 10007)) % 10007
    
    print(dp_list[-1])
    return    

if __name__ == "__main__":
    width = int(input())
    solution(width)