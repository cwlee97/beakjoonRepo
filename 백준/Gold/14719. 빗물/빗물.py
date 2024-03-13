import sys

input = sys.stdin.readline

def getInput():
    height, width = map(int, input().split(" "))
    block_list = list(map(int, input().split(" ")))

    return width, height, block_list

def solution(width, height, block_list):
    ret = 0

    for i in range(1, width-1):
        left_max = max(block_list[:i+1])
        right_max = max(block_list[i:])

        water = min(left_max, right_max) - block_list[i]

        ret += water
    
    print(ret)
        
if __name__ == "__main__":
    width, height, block_list = getInput()
    solution(width, height, block_list)