import sys
input = sys.stdin.readline
# N = 집의 개수, C = 공유기 개수
N, C = map(int, input().split()) 
coor = []
for _ in range(N):
    coor.append(int(input()))
    
coor.sort()

def binary_search(coor, start, end):
    mid = (start+end) //2
    current_coor = coor[0]
    cnt = 0
    
    while start < end:
        for i in range(len(coor)):
            if coor[i] >= current_coor + mid:
                cnt += 1
                current_coor = coor[i]
        if cnt >= C:
            ans = mid
            start = mid+1
        else:
            end = mid - 1
            
                
            
    return ans

start = 1 
end = coor[-1] - coor[0]
ans = 0


binary_search(coor, start, end)
print(ans)
