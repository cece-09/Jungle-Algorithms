import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    # 벌목된 나무 수
    high = 0
    for tree in trees:
        if tree > mid:
            high += tree - mid
    print(high)
    if high >= m:
        start = mid + 1
    else:
        end = mid - 1


print(end)


# 가져갈 수 잇는 나무 길이 리스트를 만듬 0~ 어떤 숫자 까지

# 그리고 그걸 이진탐색해서 찾아내면됨 타겟값은 m 으로
