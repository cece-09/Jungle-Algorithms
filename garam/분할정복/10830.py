import sys

input = sys.stdin.readline

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(a)
result = [[0 for _ in range(n)] for _ in range(n)]  # ex) n = 2 [[0,0][0,0]]

print(result)
