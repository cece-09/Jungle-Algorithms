import sys

input = sys.stdin.readline
temp = 0
n = int(input())
word_list = []
for i in range(n):
    word_list.append(input().strip())
    # print(word_list)
set = set(word_list)
lst = list(set)
lst.sort()

for i in lst:
    print(i)
11
