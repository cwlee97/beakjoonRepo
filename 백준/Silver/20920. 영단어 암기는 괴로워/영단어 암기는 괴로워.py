import sys
import heapq

input = sys.stdin.readline

def getInput():
    cases, min_word = map(int, input().split(" "))

    input_dict = dict()
    for _ in range(cases):
        input_word = input().rstrip()
        if len(input_word) < min_word:
            continue

        if input_word in input_dict.keys():
            input_dict[input_word] += 1
        else:
            input_dict[input_word] = 0

    return input_dict

def solution(input_dict):
    hq = list()

    for x, y in input_dict.items():
        heapq.heappush(hq, (-y, -len(x), x))
    
    for _ in range(len(input_dict)):
        print(heapq.heappop(hq)[2])

if __name__ == "__main__":
    input_dict = getInput()
    solution(input_dict)