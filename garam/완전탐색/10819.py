# from itertools import permutations
import sys
import itertools

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

per = list(itertools.permutations(arr))
max = 0


for i in per:
    sum = 0 # sum값이 for문 밖에 있으면 i의 sum값들까지도 계속 더함
    for j in range(len(i)-1): # range(0, 5) 로 하면 안됨 같은 값 같은데 왜 안될까?
        sum += abs(i[j] - i[j + 1])
        if sum > max:
            max = sum
print(max)

