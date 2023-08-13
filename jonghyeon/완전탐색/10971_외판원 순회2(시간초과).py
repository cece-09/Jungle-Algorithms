import sys
s = sys.stdin

N = int(s.readline())

W = []
for _ in range(N):
   pay = list(map(int, s.readline().split()))
   W.append(pay)

visited = [False] * N
answer = 1000000 * N

start_point = 0

def sol(start, whole_pay, route):
   global answer
   global start_point
   if sum(visited) == N:
        whole_pay += W[start][start_point]
        answer = min(answer, whole_pay)
        if answer == whole_pay:
            # print(route)
            return

   for i in range(N):
      if (start != i)  and (W[start][i] != 0) and (visited[i] == False):
        visited[i] = True
        route.append(i)
        whole_pay += W[start][i]
        sol(i, whole_pay, route)
        visited[i] = False
        route.pop()
        whole_pay -= W[start][i]

for start in range(N):
    visited[start] = True
    start_point = start
    sol(start, 0, [start])
    visited[start] = False
print(answer)