N, M = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()


def bin_search(trees, M):
    pl = 0
    pr = len(trees)-1
    
    while True:
        pc = (pl + pr) // 2
        
        if sum(trees[pc+1:]) - trees[pc]*(pr - pc) == M:
            return trees[pc]
            
        elif sum(trees[pc+1:]) - trees[pc]*(pr - pc) > M:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr:
            break

    sum_targets = sum(trees[pl:])
    cnt_targets = len(trees)- pl
    
    candidate = range(trees[pc]+1, trees[pl])
    pl = 0
    pr = len(candidate) -1

    while True:
        pc = (pl + pr) // 2
        if sum_targets - candidate[pc]*cnt_targets == M:
            return candidate[pc]
        elif sum_targets - candidate[pc]*cnt_targets > M:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return candidate[pc]

print(bin_search(trees, M))
