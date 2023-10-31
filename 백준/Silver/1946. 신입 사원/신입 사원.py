import sys
from collections import deque

input = sys.stdin.readline

cases = int(input())

for _ in range(cases):
    num_of_people = int(input())
    people_list = list()
    min_rank = 0
    answer = 0

    for _ in range(num_of_people):
        people_list.append(list(map(int, input().split(" "))))

    people_list.sort(key=lambda x : x[0])

    people_queue = deque(people_list)

    while people_queue:
        people = people_queue.popleft()
        if min_rank == 0:
            min_rank = people[1]
            answer += 1
            continue
            
        if people[1] < min_rank:
            min_rank = people[1]
            answer += 1
        
    print(answer)