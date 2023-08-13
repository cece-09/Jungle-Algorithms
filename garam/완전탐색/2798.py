import sys

input = sys.stdin.readline

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0
# print(card_list)

for i in range(len(card_list)):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if card_list[i] + card_list[j] + card_list[k] > m:
                continue
            else:
                result = max(result, card_list[i] + card_list[j] + card_list[k])
print(result)
