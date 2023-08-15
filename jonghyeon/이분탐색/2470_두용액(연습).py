import sys
from math import inf
input = sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())))
def binary_search(A):
    i = 0
    j = len(A)-1
    r = inf
    while i < j:
        tmp = A[i]+A[j]
        if tmp == 0:
            return A[i], A[j]
        if abs(tmp) < r:
            result = (A[i], A[j])
            r = abs(tmp)
        if tmp > 0:
            j -= 1
        else:
            i += 1
    return result
result = binary_search(A)
print(result[0], result[1])


# n = int(input())
# array = list(map(int, input().split()))
# array.sort()

# start = 0
# end = len(array) - 1
# answer = answer = abs(array[start] + array[end]) # 또는 1e9?(많이 큰 숫자 또는 나올수있는 특성값 중 아무거 모두 가능)

# def binary_search(array, start, end):
#     global answer
#     while start < end:
#         mid_x_two = array[start] + array[end]

#         if mid_x_two == 0:
#             result = (array[start], array[end])
#             break
        
#         if abs(mid_x_two) < answer:
#             result = (array[start], array[end])
#             answer = abs(mid_x_two)
#         if mid_x_two > 0:
#             end -= 1
#         else:
#             start += 1
#     return result

# print(binary_search(array, start, end))