import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2

    # 벌목된 나무 수
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    print(f'total =  {total}')

    if total >= m:
        start = mid + 1
        print(f'start = {start}')
        print(end)
    else:
        end = mid - 1
        print(start)
        print(end)

print(end)

