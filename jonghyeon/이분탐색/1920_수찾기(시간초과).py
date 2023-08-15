N = int(input())
A = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
    if x in A:
        print(1)
    else:
        print(0)