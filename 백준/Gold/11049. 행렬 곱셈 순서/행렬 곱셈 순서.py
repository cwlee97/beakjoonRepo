import sys

input = sys.stdin.readline

def func(num_of_matrix, row, col):
    count_array = [[0 for _ in range(num_of_matrix)]for _ in range(num_of_matrix)]

    for size in range(1, num_of_matrix):
        for start in range(0, num_of_matrix - size):
            end = start + size

            count_array[start][end] = 2**31

            for middle in range(start, end):

                count_array[start][end] = min(
                    count_array[start][middle] + count_array[middle+1][end] + row[start] * col[middle] * col[end],
                    count_array[start][end]
                    )

    return count_array

if __name__ == "__main__":
    num_of_matrix = int(input())
    row, col = [None for _ in range(num_of_matrix)], [None for _ in range(num_of_matrix)]

    for i in range(num_of_matrix):
        row[i], col[i] = map(int, input().split(" "))

    count_array = func(num_of_matrix, row, col)

    print(count_array[0][-1])