import sys

input = sys.stdin.readline
N, C = list(map(int, input().split()))
coor = sorted([int(input()) for _ in range(N)])
start = 1
end = coor[N - 1] - coor[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    current = coor[0]
    cnt = 1

    for i in range(1, N):
        if coor[i] >= current + mid:
            current = coor[i]
            cnt += 1
    if cnt >= C:
        start = mid +1
        ans = mid
    else:
        end = mid-1
print(ans)
