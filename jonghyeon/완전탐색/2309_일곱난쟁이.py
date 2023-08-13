import sys

heights = [int(sys.stdin.readline().strip()) for _ in range(9)]

differ = sum(heights) - 100

for i in range(9):
    if differ/2 != heights[i]:
        flag = 0
        for j in range(9):
            if heights[j] + heights[i] == differ:
                heights.remove(heights[j])
                heights.remove(heights[i])
                flag = 1
                break
        if flag == 1:
            break

heights.sort()
for i in heights:
    print(i)
