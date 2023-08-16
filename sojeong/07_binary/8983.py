import sys


def attackable3(x, y):
    s, e = x-(L-y), x+(L-y)
    for i in range(s, e+1):
        if i in m:
            return True
    return False


def attackable2(x, y):
    s, e = x-(L-y), x+(L-y)
    if s == e:
        return s in m
    i, j, k = 0, M-1, 0
    # two pointer로 m[i] < s 이거나 m[i] > e 인 인덱스 검색
    while k < M:
        if m[i] < s:
            i += 1
        if m[j] > e:
            j -= 1
        if i >= j:
            break
        k += 1
    if i > j:
        return False
    if i == j:
        if i == s or i == e:
            return False
        # 만난 값이 (s, e)에 속하는지 반환
        return s <= m[i] <= e
    return True


def attackable(x, y):
    s, e = x-(L-y), x+(L-y)

    if m[M-1] <= s:
        if m[M-1] == s:
            return True  # s의 lower bound를 구할 것이므로 같은 경우까지 처리
        return False  # 범위 (s, e)는 배열의 오른쪽에 있음
    if m[0] > e:
        # if m[0] == e:  # e의 upper bound를 구할 것이므로 같은 경우까지 처리
        #     return True
        return False  # 범위 (s, e)는 배열의 왼쪽에 있음
    if s == e:
        return s in m  # 만약 s = e이면 이 점이 사대인지만 확인

    v1, v2 = -1, M
    # m[i] >= s 인 최소의 값 v1 탐색: lower bound
    # s보다 크거나 같은 수가 처음 등장하는 위치를 찾는다
    low, high = 0, M-1
    while low+1 < high:  # low와 high 사이에는 한 칸 존재
        mid = (low+high)//2
        if m[mid] >= s:  # if true
            high = mid
        else:
            low = mid
    v1 = high

    # m[i] > e 인 최소의 값 v2 탐색: upper bound
    # e보다 큰 수가 처음 등장하는 위치를 찾는다
    # 찾은 후 high-1 하면 e보다 작거나 같은 수의 최대 인덱스가 된다
    low, high = 0, M-1
    while low+1 < high:
        mid = (low+high)//2
        if m[mid] > e:  # if true
            high = mid
        else:
            low = mid
    v2 = high-1

    # 만약 v1 > v2라면 범위는 없다
    if v1 > v2:
        return True
    return False


M, N, L = map(int, input().split())
m = list(map(int, input().split()))
n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


m.sort()
lower = m[0]-L
upper = m[-1]-L

excp = 0
# y좌표가 L을 초과하면 제외
# 모든 점에 대해 사정거리 안에 있는지 여부 조사
for i in range(N):
    if n[i][1] > L:
        # print(f"EXCEPT: ({n[i][0]}, {n[i][1]})")
        excp += 1
        continue
    if not attackable(n[i][0], n[i][1]):
        # print(f"EXCEPT: ({n[i][0]}, {n[i][1]})")
        excp += 1

print(N-excp)
