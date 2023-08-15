# 두 용액
import sys
import itertools

# from itertools import permutations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

srr = list(itertools.permutations(arr, 2))
print(srr)
brr = []

for s in srr:
    brr.append(sum(s))

srr = list(set([tuple(set(srr)) for srr in srr]))
# srr = set(srr)
brr = set(brr)
brr = list(brr)
brr.sort()
# brr.sort()

print(f"srr = {srr}")

print(f"\nbrr 비알알  = {brr}")
