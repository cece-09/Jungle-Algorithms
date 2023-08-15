# 두 용액 투포인터 활용
import sys
import itertools
# from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = n - 1
max = 1e9
ans_1 = 0
ans_2 = 0

while start < end:
    temp = arr[start] + arr[end]
    abs_temp = abs(temp)
    if max > abs_temp:
        max = abs_temp
        ans_1 = arr[start]
        ans_2 = arr[end]
# 이 부분이 헷갈리는데 0보다 크면 양수쪽을 줄여야 함
    if temp > 0:
        end -= 1
    else:
        start += 1
        
print(ans_1, ans_2)