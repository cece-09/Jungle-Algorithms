N, B = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

def mul(n, matrix1, matrix2):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result

def solution(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix, matrix)
    else:
        temp = solution(n, b//2, matrix)
        if b % 2 == 0:
            return mul(n, temp, temp)
        else:
            return mul(n, mul(n, temp, temp), matrix)
        
result = solution(N, B, A)

for row in result:
    for num in row:
        # print(num, end= ' ')
        print(num%1000, end=' ')
    print()