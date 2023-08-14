# 행렬 제곱
import sys
input = sys.stdin.readline
c = 1000
# 행렬 곱셈과 같은 방식
def mat_mul(mat_a, mat_b):
    N = len(mat_a)
    result = [[0 for _ in range(N)] for _ in range(N)] # ex) n = 2 [[0,0][0,0]]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
                # 큰 수의 연산에 따른 시간초과를 막기 위함
                result[i][j] %= c
    return result

def mat_pow(mat_A, B):
    if B == 1:
        return mat_A
    else:
        tmp = mat_pow(mat_A, B // 2)
        if B % 2 == 0:
            return mat_mul(tmp, tmp)
        else:
            return mat_mul(mat_A, mat_mul(tmp, tmp))

# 출력 부분
N, B = map(int, input().split())  # N = 행렬 크기 B = 몇번 제곱 하는지
mat_A = [list(map(int, input().split())) for _ in range(N)]
result = mat_pow(mat_A, B)
for i in result:
    for j in i:
        print(j % c, end=" ")
    print()
