import time
B = [10, 8, 7, 6, 5]

def solution_b(x):
    start_time = time.time()
    sort_list = sorted(x, reverse=True)
    while sort_list[1] != 0:
        sort_list[0] = sort_list[0] - sort_list[1]
        sort_list[1] = 0
        sort_list = sorted(sort_list, reverse=True)
    end_time = time.time()
    return sum(sort_list), start_time, end_time


re, st, et = solution_b(B)