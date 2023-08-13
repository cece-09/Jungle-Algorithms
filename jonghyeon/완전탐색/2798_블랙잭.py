import sys

N, M = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

cards.sort()

min_differ = M
candidate = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_num = cards[i] + cards[j] + cards[k]
            if (M - sum_num >= 0) and (min_differ > M - sum_num):
                min_differ = M - sum_num
                candidate = sum_num

print(candidate)