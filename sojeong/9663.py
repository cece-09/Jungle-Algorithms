# N Queen

import sys
sys.setrecursionlimit(10**8)


def attackable(i, q):
    for r, col in enumerate(cols):
        if col == None:
            continue
        if col == i:
            return True
        if abs(col-i) == abs(q-r):
            return True
    return False


def queen(q):
    global cnt
    if q == N:
        if None in cols:
            return
        cnt += 1
        return
    for i in range(N):
        if attackable(i, q):
            if i == N-1:
                return
            continue
        cols[q] = i
        queen(q+1)
        cols[q] = None


N = int(input())
if N == 2 or N == 3:
    print(0)

else:
    cnt = 0
    cols = [None for _ in range(N)]
    queen(0)
    print(cnt)
