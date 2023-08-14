# 분할, 재귀로 연산 횟수 줄이기!
import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())


def multi(a, n):
    if n == 1:
        return a % c
    else:
        temp = multi(a, n // 2)
        if n % 2 == 0:                   # 짝수라면
            return (temp * temp) % c

        else:                            # 홀수라면
            return (temp * temp * a) % c
        
print(multi(a,b))
