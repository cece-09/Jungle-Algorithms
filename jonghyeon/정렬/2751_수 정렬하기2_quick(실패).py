#### 1

# import sys

# def quick_sort(arr, low, high):
#     """
#     arr : array [List]
#     low : 정렬 할 가장 왼쪽값의 index [INT]
#     hight : 정렬 할 가장 오른값의 index [INT]
#     """
#     if low < high:
#         pivot = partition(arr, low, high)
#         quick_sort(arr, low, pivot-1)
#         quick_sort(arr, pivot+1, high)
#     return arr


# def partition(a, pivot, high):
#     """
#     a : array [List]
#     pivot : pivot값의 index [INT]
#     hight : 정렬 할 가장 오른값의 index [INT]
#     """
#     i = pivot + 1
#     j = high
#     while True:
#         while i < high and a[i] < a[pivot]:
#             i += 1
#         while j > pivot and a[j] > a[pivot]:
#             j -= 1
#         if j <= i:
#             break
#         a[i], a[j] = a[j], a[i]
#         i += 1
#         j -= 1

#     a[pivot], a[j] = a[j], a[pivot]
#     return j

# N = int(sys.stdin.readline().strip())

# unsorted = []
# for _ in range(N):
#     unsorted.append(int(sys.stdin.readline().strip()))

# quick_sort(unsorted, 0, len(unsorted)-1)

# for i in unsorted:
#     print(i)



#### 2
# import sys

# def quicksort(A, lo, hi):
#     def partition(lo, hi):
#         pivot = A[hi]
#         left = lo
#         for right in range(lo, hi):
#             if A[right] < pivot:
#                 A[left], A[right] = A[right], A[left]
#                 left += 1

#         A[left], A[hi] = A[hi], A[left]
#         return left
    
#     if lo < hi:
#         pivot = partition(lo, hi)
#         quicksort(A, lo, pivot - 1)
#         quicksort(A, pivot + 1, hi)


# N = int(sys.stdin.readline().strip())

# unsorted = []
# for _ in range(N):
#     unsorted.append(int(sys.stdin.readline().strip()))

# quicksort(unsorted, 0, len(unsorted)-1)

# for i in unsorted:
#     print(i)

### 3
import sys

def quicksort(A, lo, hi):
    if lo < hi:
        pivot = partition(A, lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    left = lo
    for right in range(lo, hi):
        if A[right] < pivot:
            A[left], A[right] = A[right], A[left]
            left += 1

    A[left], A[hi] = A[hi], A[left]
    return left


N = int(input())

unsorted = []
for _ in range(N):
    unsorted.append(int(input()))

quicksort(unsorted, 0, len(unsorted)-1)

for i in unsorted:
    print(i)