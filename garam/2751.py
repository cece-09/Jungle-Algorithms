# import sys

# input = sys.stdin.readline

# num = int(input())
# arr = []
# for i in range(num):
#     arr.append(int(input()))
# arr.sort()
# for i in range(num):
#     print(arr[i])
    
import sys

input = sys.stdin.readline

num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))

for i in sorted(arr):
    print(i)

