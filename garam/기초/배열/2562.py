# arr = [int(input()) for i in range(9)]
# print(max(arr))
# print(arr.index(max(arr))+1)

arr = []
for i in range(9):
    arr.append(int(input()))
max = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        j = i+1
print(max)
print(j)
