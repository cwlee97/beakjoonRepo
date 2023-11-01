import sys
import heapq

input = sys.stdin.readline

def get_input():
    multitap_length, num_of_part = map(int, input().split(" "))
    part_list = list(map(int, input().split(" ")))

    return multitap_length, num_of_part, part_list

def solution(multitap_length, num_of_part, part_list):
    multitap = list()
    answer = 0

    for part_idx in range(len(part_list)):
        if part_list[part_idx] in multitap:
            continue
        elif len(multitap) < multitap_length:
            multitap.append(part_list[part_idx])
        else:
            part_info = list()
            for using_part in multitap:
                try:
                    part_info.append([-(part_idx + part_list[part_idx+1:].index(using_part)), using_part])
                except:
                    part_info.append([-num_of_part, using_part])

            heapq.heapify(part_info)
            multitap.remove(heapq.heappop(part_info)[1])
            multitap.append(part_list[part_idx])
            answer += 1
    return answer


if __name__ == "__main__":
    multitap_length, num_of_part, part_list = get_input()
    answer = solution(multitap_length, num_of_part, part_list)
    print(answer)
