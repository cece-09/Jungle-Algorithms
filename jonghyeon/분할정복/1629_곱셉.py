A, B, C = map(int, input().split())

# 1. B 줄여주기
# (A**B)%C
# ((A**(B//2))**2) %C   # B 짝수였을때
# ((A**(B//2))**2)*A %C # B 홀수였을때

# 2. mod
# (A**B)%C
# ((A%C)**B)%C

def solution(A, B, C):
    if B == 1:
        return A%C  #2
    
    if B % 2 == 0:
        return (solution(A, B//2, C)**2) % C    #1
    else:
        return (solution(A, B//2, C)**2)*A % C  #1
    

print(solution(A, B, C))