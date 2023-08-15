N = int(input())
A = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))


def bin_search(a, key):
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return 1
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr:
            break
    
    return 0


A.sort()
for x in numbers:
    print(bin_search(A, x))