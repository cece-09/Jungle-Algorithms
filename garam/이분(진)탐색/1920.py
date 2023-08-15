import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
target_arr = list(map(int, input().split()))

def binary_search(target_num, data):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if target_num == data[mid]:
            return True
        elif target_num < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

# 톱길이랑 잘린 나무의 길이는 반비레


for num in target_arr:
    if binary_search(num, arr):
        print(1)
    else:
        print(0)



# 시간초과 난 답

# n = map(int, input().split())
# arr = list(map(int, input().split()))
# m = map(int, input().split())
# brr = list(map(int, input().split()))
# crr = [0 for i in range(len(arr))]  # n으로 하니까 안되네;;
# arr.sort()

# for i in range(len(brr)):
#     for j in range(len(brr)):
#         if brr[i] == arr[j]:
#             crr[i] = 1
# for num in crr:
#     print(num)

# 시간초과는 아니지만 이진탐색이 아닌 경우
# n = map(int, input().split())
# arr = set(map(int, input().split()))
# m = map(int, input().split())
# brr = list(map(int, input().split()))
# crr = [0 for i in range(len(arr))]  # n으로 하니까 안되네;;

# for num in brr:
#     if num in arr:
#         print(1)
#     else:
#         print(0)
