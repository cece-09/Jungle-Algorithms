import sys

input = sys.stdin.readline
hansu = 0

# n = list(map(int, input().strip()))

n = int(input().strip())
for i in range(1, n + 1):
    if i < 100:
        hansu += 1
    # print(hansu)
    elif i >= 100:
        # if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
        a = int(str(i)[0]) - int(str(i)[1])
        b = int(str(i)[1]) - int(str(i)[2])
        if a == b:
            hansu += 1
print(hansu)
