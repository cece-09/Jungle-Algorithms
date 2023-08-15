import sys

input = sys.stdin.readline

n, k = map(int, input().split())
x_arr = list(int(input()) for _ in range(n))

# start와 end값을 무엇으로 할지 결정하는게 가장 어렵다. 내가 무엇을 구하고 싶은지 명확하게 하는게 힘들어
start = min(x_arr)
end = start + k
ans = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for x in x_arr:
        if x <= mid:
            temp += mid - x
    if temp <= k:
        start = mid + 1
        ans = max(mid, ans)
    else:
        end = mid - 1
print(ans)
