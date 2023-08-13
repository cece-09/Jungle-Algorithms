import sys

N = int(sys.stdin.readline().strip())

words = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    words.append((len(word), word))

words_list = list(set(words))
words_list.sort()
for len, word in words_list:
    print(word)