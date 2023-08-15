'''
X1 = 10     X2 = 20     X3 = 15
     17                      17
'''
import sys

n, k = map(int, input().split())
levels = [int(sys.stdin.readline()) for _ in range(n)]

levels.sort()

left, right = levels[0], levels[-1] + k

def get_diff(mid):
    diff = 0
    for level in levels:
        if level < mid:
            diff += mid - level
        else:
            break
    return diff

while left <= right:
    mid = (left + right) // 2
    diff = get_diff(mid)
    if diff <= k:
        left = mid+1
    else:
        right = mid-1

print(right)


# current = 0
# possible = K

# if N == 1:
#     level[current] += K
#     print(level[current])
# else:
#     while possible > 0:
#         while True:
#             if current == len(level)-1:
#                 break

#             if level[current] >= level[current + 1]:
#                 current += 1
#                 continue
#             if level[current] == 

#             level[current] += 1
#             possible -= 1
#             break
        
#         level[current] += 1
#         possible -= 1


#         if level[current] < level[current + 1]:
#         level[current] += 1
#         possible -= 1
