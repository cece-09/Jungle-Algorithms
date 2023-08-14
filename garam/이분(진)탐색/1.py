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
            start = mid - 1
    return False


for num in target_arr:
    if binary_search(num, arr):
        print(1)
    else:
        print(0)
