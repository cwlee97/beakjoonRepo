import sys

input = sys.stdin.readline

if __name__ == "__main__":
    str1 = input().rstrip()
    str2 = input().rstrip()

    LCS_array = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str1[j-1] == str2[i-1]:
                LCS_array[i][j] = LCS_array[i-1][j-1]+1
            else:
                LCS_array[i][j] = max(LCS_array[i - 1][j], LCS_array[i][j - 1])

    print(LCS_array[-1][-1])