n = int(input())
for i in range(n):
    m, s = input().split()
    m = int(m)
    for j in s:
        print(m*j, end="")
    print()
