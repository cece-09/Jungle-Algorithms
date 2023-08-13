import sys, itertools
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
card_list = list(map(str, input().split()))
# print(card_list)

biggest_sum = 0
cards_set = list(map("".join, itertools.permutations(card_list, 3)))

for cards in cards_set:
    temp_sum = sum(cards)
    if biggest_sum < temp_sum <= m:
        biggest_sum = temp_sum
print(biggest_sum)
