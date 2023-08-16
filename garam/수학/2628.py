x, y = map(int, input().split())
x_list = [0, x]
y_list = [0, y]

n = int(input())
for i in range(n):
    xy, length = map(int, input().split())
    if xy == 0:
        y_list.append(length)
    else:
        x_list.append(length)
x_list.sort()
y_list.sort()

ans = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i - 1]
        height = y_list[j] - y_list[j - 1]
        ans = max(ans, width * height)
print(ans)
