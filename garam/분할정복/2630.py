import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().strip().split())) for i in range(n)]
ans = []

def solution(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return 0
    if color == 0:
        ans.append(0)
    else:
        ans.append(1)

solution(0, 0, n)
print(f"ans 입니다. : {ans}")
print(ans.count(0))
print(ans.count(1))
