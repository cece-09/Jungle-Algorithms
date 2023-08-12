#Merge Sort

import sys

def merge_sort(arr):
    """
    arr : 정렬 할 배열 
    ---
    return :  정렬 된 배열
    """
    if len(arr) <= 1: # 종료조건
        return arr 
    mid = len(arr) // 2
    
    leftList = arr[:mid]
    rightList = arr[mid:]

    leftList = merge_sort(leftList) # sort
    rightList = merge_sort(rightList) # sort
    
    mergedList = merge(leftList,rightList)
    return mergedList

def merge(left, right):
    # leftList, rightList는 이미 정렬이 되어있다.
    mergedList = []
    total_len = len(left) + len(right)

    while len(mergedList) < total_len:
        if len(left) > 0 and len(right) > 0 : 
            # left & right 모두 하나 이상의 값이 남아있을때는 비교
            if left[0] <= right[0]:
                mergedList.append(left.pop(0))
            else:
                mergedList.append(right.pop(0))

        elif len(left) == 0:
            # 왼쪽 리스트가 비어있다면 그래도 오른쪽 리스트를 붙이기
            mergedList += right

        elif len(right) == 0:
            # 오른쪽 리스트가 비어있다면 그래도 왼쪽 리스트를 붙이기
            mergedList += left
    return mergedList


N = int(sys.stdin.readline().strip())

unsorted = []
for _ in range(N):
    unsorted.append(int(sys.stdin.readline().strip()))

result = merge_sort(unsorted)

for i in result:
    print(i)