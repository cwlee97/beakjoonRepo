import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    num_of_meeting = int(input())
    meeting_list = list()

    for _ in range(num_of_meeting):
        start, end = map(int, input().split(" "))
        meeting_list.append((start, end))

    meeting_list.sort(key=lambda x: (x[1], x[0]))

    meeting_queue = deque(meeting_list)

    end_time = 0
    answer = 0

    while meeting_queue:
        meeting = meeting_queue.popleft()
        if end_time == 0:
            end_time = meeting[1]
            answer += 1
            continue
        if meeting[0] >= end_time:
            end_time = meeting[1]
            answer += 1

    print(answer)