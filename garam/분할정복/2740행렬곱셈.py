# 행렬 제곱전에 풀어보면 좋을거 같아서~~

# 입력
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

# 행렬 곱셉
c = [[0 for _ in range(k)] for _ in range(n)]  # 해당 크기의 행렬을 0값을 넣어 미리 만들어준 뒤 값을 넣을 예정
for i in range(n):
    for j in range(k):
        for h in range(m):
            c[i][j] += a[i][h] * b[h][j]
# 출력
for i in c:
    for j in i:
        print(j, end=" ")
    print()
