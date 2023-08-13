import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
sum_list = []

for _ in permutations(card_list, 3):
    if sum(_) > m:
        continue
    else:
        sum_list.append(sum(_))
print(max(sum_list))