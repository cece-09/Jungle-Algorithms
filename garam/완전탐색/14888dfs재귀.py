# 14888번 연산자 끼워 놓기
# dfs 이용
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split()) # 왜 리스트 안 만듬?

max_value = -1e9 # 인피닛이 아니면 보통 이렇게 다 줌
min_value = 1e9
# dfs 매서드 정의
def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value
    # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        # 더하기
        if add > 0:
            # print(add) 1
            add -= 1
            # print(add) 0
            dfs(i + 1, arr + data[i])
            # print(add) 0
            add += 1 # 원상복귀 시키는 시점이 궁금함 재귀가 끝나고???
            # print(add) 1
        # 빼기
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - data[i])
            sub += 1
        # 곱하기
        if mul > 0:
            mul -= 1
            dfs(i + 1, arr * data[i])
            mul += 1
        # 나누기
        if div > 0:
            div -= 1
            dfs(i + 1, int(arr / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)
