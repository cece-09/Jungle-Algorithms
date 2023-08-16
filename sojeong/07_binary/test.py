import sys


def attackable(x, y, arr):
    s, e = x, y

    # 만약 s = e이면 이 점이 사대인지만 확인
    if s == e:
        return s in m

    v1, v2 = -1, len(arr)
    # m[i] < s 인 최대의 값 탐색
    i, j = 0, len(arr)-1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] >= s:
            j = mid - 1
        else:
            v1 = max(v1, mid)
            i = mid + 1

    # m[i] > e 인 최소의 값 탐색
    i, j = 0, len(arr)-1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] <= e:
            i = mid + 1
        else:
            v2 = min(v2, mid)
            j = mid - 1

    print(f"FOUND: {v1}, {v2}")
    # 검색 결과에 따라 T/F 반환
    if v2-v1 <= 1:
        if m[v2] <= e or m[v1] >= s:
            return True
        return False  # v1과 v2 사이에 값이 없음
    return True


M, N, L = map(int, input().split())
m = list(map(int, input().split()))
n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
