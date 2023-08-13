import sys
input = input
def calculate(x, y, o):
    if o == 0:
        return x + y
    if o == 1:
        return x - y
    if o == 2:
        return x * y
    if o == 3:
        if x < 0 and y > 0:
            return (-x // y) * -1
        return x // y

def operation(i, rs):
    global minr, maxr
    if i == N - 1:
        if maxr == None or rs > maxr:
            maxr = rs
        if minr == None or rs < minr:
            minr = rs
        return
    for j in range(4): # [0, 1, 2, 3]
        if O[j] > 0:
            O[j] -= 1
            print(O[j])
            operation(i + 1, calculate(rs, A[i + 1], j))
            O[j] += 1

# +, -, *, // 중
# N-1개의 연산자를 순서를 고려하여 선택합니다.
# 중복 허용
N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))
print(f"A = {A}")
print(f"O = {O}")

minr, maxr = None, None

operation(0, A[0])
print(maxr)
print(minr)
