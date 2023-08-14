import sys
s = sys.stdin

N = int(s.readline())

W = [list(map(int, input().split()))for _ in range(N)]

visited = [0] * N
answer = sys.maxsize

start_point = 0

def sol(start, whole_pay, cnt):
   global answer

   if cnt == N:
      if W[start][start_point] != 0:
         whole_pay += W[start][start_point]
         answer = min(answer, whole_pay)

      return
   if whole_pay > answer:
      return

   for i in range(N):
      if (W[start][i] != 0) and (visited[i] == 0):
        visited[i] = 1
        sol(i, whole_pay + W[start][i], cnt + 1)
        visited[i] = 0

for start in range(N):
    visited[start] = 1
    start_point = start
    sol(start, 0, 1)
    visited[start] = 0
print(answer)