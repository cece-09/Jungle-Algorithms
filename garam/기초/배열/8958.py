n = int(input())
# arr = [list(map(str, input().split())) for i in range(n)]
arr = [input() for i in range(n)]

for a in arr:
    total = 0
    score = 0
    for i in range(len(a)):
        if a[i] == "O":
            score += 1
            total += score
        else:
            score = 0
    print(total)
