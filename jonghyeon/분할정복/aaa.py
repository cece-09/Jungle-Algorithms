# Closest Pair
import sys
import math


def distance(d1: tuple, d2: tuple):  # 거리 제곱
    return (d1[0]-d2[0])**2 + (d1[1]-d2[1])**2


def closest_pair(s, e):
    global mindist
    if e - s == 1:
        return
    if e - s == 2:
        d = distance(D[I[s]], D[I[e-1]])
        if mindist == None or mindist > d:
            mindist = d
        return

    # x좌표의 mid값 구하기
    mid = (s + e) // 2

    closest_pair(s, mid)
    closest_pair(mid, e)
    d = mindist

    # mid-d < x < mid+d 점 (중간 영역) 조사
    for i in range(mid, s-1, -1):
        if D[I[mid]][0] - D[I[i]][0] > math.sqrt(d):
            break
    for j in range(mid, e):
        if D[I[j]][0] - D[I[mid]][0] > math.sqrt(d):
            break

    # i~j 중간 영역에서의 최근접점 조사
    mids = sorted(I[i:j+1], key=lambda d: D[d][1], reverse=True)
    for p in range(len(mids)-1):
        for q in range(p+1, len(mids)):
            if D[mids[q]][1] - D[mids[p]][1] >= math.sqrt(d):
                break
            mindist = min(mindist, distance(D[mids[p]], D[mids[q]]))

    # 0~mid에서 y절댓값이 가장 작은 점의 인덱스
    # l = I.index(min(I[s:mid], key=lambda d: abs(D[d][1])))
    # r = I.index(min(I[mid:e], key=lambda d: abs(D[d][1])))

    # l~r 사이에서 최솟값 구하기
    # for i in range(l, r+1):
    #     for j in range(i+1, r+1):
    #         if mindist == None or distance(D[i], D[j]) < mindist:
    #             mindist = distance(D[i], D[j])

    return


# 입력을 받음
N = int(input())
D = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
I = [i for i in range(N)]  # 좌표의 인덱스 배열
mindist = None

# D배열의 x좌표값을 기준으로 I배열 정렬
I.sort(key=lambda i: D[i][0])

# 재귀 호출
closest_pair(0, N)
print(mindist)