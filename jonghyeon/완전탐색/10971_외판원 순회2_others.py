import sys


N = int(input())

W = [list(map(int, input().split()))for _ in range(N)]

visited = [0] * N
answer = sys.maxsize



def sol(start_point, start, whole_pay, cnt):
    global answer
    if cnt == N:
        if W[start][start_point]:
            whole_pay += W[start][start_point]
            if answer > whole_pay:
                answer = whole_pay
        return

    if whole_pay > answer:
        return

    for i in range(N):
        if not visited[i] and W[start][i]:
            visited[i] = 1
            sol(start_point, i, whole_pay + W[start][i], cnt + 1)
            visited[i] = 0


for i in range(N):
    visited[i] = 1
    sol(i, i, 0, 1)
    visited[i] = 0
print(answer)