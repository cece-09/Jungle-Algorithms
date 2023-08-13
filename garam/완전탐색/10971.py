import sys
import itertools

input = sys.stdin.readline
arr = []
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))

print(arr)
