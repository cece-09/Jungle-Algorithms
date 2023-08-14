# 행렬 제곱전에 풀어보면 좋을거 같아서~~

# 입력
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

# 행렬 곱셉
C = [[0 for _ in range(K)] for _ in range(N)]  # 해당 크기의 행렬에 0값을 넣어 미리 만들어준 뒤 값을 넣을 예정
for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]
# 출력
for i in C:
    for j in i:
        print(j, end=" ")
    print()
