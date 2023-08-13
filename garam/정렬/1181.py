import sys
input = sys.stdin.readline

n = int(input())
word_list = []
for i in range(n):
    word_list.append(input().strip())
    # print(word_list)
set = set(word_list)
lst = list(set)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
