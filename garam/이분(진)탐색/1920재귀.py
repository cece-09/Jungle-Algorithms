import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
target_arr = list(map(int, input().split()))

def binary_search(data, target, start, end):
    if start > end:  # while이랑 다르게 >= 이 아니라 >
        return False
    mid = (start+end) // 2
    if target == data[mid]:
        return True
    elif target > data[mid]:
        return binary_search(data, target, mid+1, end)
    else:
        return binary_search(data, target, start, mid-1)
    

for target in target_arr:
    if binary_search(arr, target, 0, n-1):
        print(1)
    else:
        print(0)
