import sys

input = sys.stdin.readline
n, k = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))
# x = list(map(int, input().split()) for _ in range(n)) # 이거 안되는데 어떻게 위 코드를 줄일 수 있지?

print(n, k)
print(x)
