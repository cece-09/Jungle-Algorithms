import sys

N = int(sys.stdin.readline().strip())
f = [None] * 51

for _ in range(N):
    word = sys.stdin.readline().strip()
    if f[len(word)] == None:
        f[len(word)] = [word]
    else:
        for i in range(len(f[len(word)])):
            if f[len(word)][i] < word:
                continue
            elif f[len(word)][i] == word:
                break
            else:
                f[len(word)].insert(i, word)
                break


for i in range(51):
    if f[i] != None:
        for word in f[i]:
            print(word)
