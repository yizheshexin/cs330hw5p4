import numpy as np
import time
A = [10, 7, 4, 4]


def solution_a(x):
    start_time = time.time()
    sum_all = sum(x)
    col_num = sum(x) + 1
    row_num = len(x)
    result = np.zeros(row_num,dtype = 'int8')
    matrix = np.zeros([row_num,col_num],dtype = 'int64')
    for each in range(row_num):
        matrix[each][0] = 1
    matrix[0][x[0]] = 1
    for row_count in range(1,row_num):
        for col_count in range(col_num):
            elem = matrix[row_count - 1][col_count]
            if elem == 1:
                matrix[row_count][col_count] = 1
                matrix[row_count][col_count + x[row_count]] = 1
    diff = col_num
    for each in range(col_num):
        if matrix[row_num-1][each] == 1:
            if abs(((sum_all / 2) - each)) < diff:
                diff = abs(((sum_all / 2) - each))
                mid = each
    for each in reversed(range(row_num)):
        if each >= 1:
            if matrix[each][mid] == matrix[each - 1][mid]:
                result[each] = 1  # buxuan
            else:
                result[each] = -1  # xuan
                mid = mid - x[each]
        else:
            if x[each] == mid:
                result[each] = -1
            else:
                result[each] = 1
    end_time = time.time()
    return sum(result * x), start_time , end_time


re, t1 , t2 = solution_a(A)




