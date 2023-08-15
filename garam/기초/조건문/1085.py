x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))


# arr = list(map(int, input().split()))
# print(arr)
# a = arr[2] - arr[0]
# b = arr[3] - arr[1]
# c = arr[0] - 0
# d = arr[1] - 0
# t = min(a, b, c, d)
# print(t)
