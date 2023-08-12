import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = []
for _ in range(n):
    cards.append(sys.stdin.readline().strip())

# [1, 2, 12, 1]

result = set()

def pick(cards_left, select_num, string):
    if select_num == 0:
        result.add(string)
        return

    for i in range(len(cards_left)):
        cards_present = cards_left.copy()
        string_present = string + cards_present.pop(i)
        pick(cards_present, select_num - 1, string_present)

pick(cards, k, '')


print(len(result))