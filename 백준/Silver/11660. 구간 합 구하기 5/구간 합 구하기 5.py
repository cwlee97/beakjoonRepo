import sys

input = sys.stdin.readline

def getInput():
    size, cases = map(int, input().split(" "))

    array = list()
    for _ in range(size):
        array.append(list(map(int, input().split(" "))))

    dp_array = [[0 for _ in range(size)] for _ in range(size)]
    
    dp_array[0][0] = array[0][0]
    for i in range(1, size):
        dp_array[i][0] = array[i][0] + dp_array[i-1][0]
        dp_array[0][i] = array[0][i] + dp_array[0][i-1]
    for i in range(1, size):
        for j in range(1, size):
            dp_array[i][j] = dp_array[i-1][j] + dp_array[i][j-1] - dp_array[i-1][j-1] + array[i][j]
    
    xy_array = list()
    for _ in range(cases):
        xy_array.append(list(map(int, input().split(" "))))

    return dp_array, xy_array

def solution(dp_array, xy_array):
    for element in xy_array:
        x1, y1, x2, y2 = element

        res = dp_array[x2-1][y2-1]

        if x1-2 >= 0:
            res -= dp_array[x1-2][y2-1]
        
        if y1-2 >= 0:
            res -= dp_array[x2-1][y1-2]
        
        if x1-2 >= 0 and y1 -2 >= 0:
            res += dp_array[x1-2][y1-2]

        print(res)
    return 0
    
    


if __name__ == "__main__":
    dp_array, xy_array = getInput()
    solution(dp_array, xy_array)