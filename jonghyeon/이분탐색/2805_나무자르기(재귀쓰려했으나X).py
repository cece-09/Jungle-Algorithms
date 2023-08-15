N, M = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()


flag = 0
target_idx = 0
target_idx_limit = 0


def bin_search(range, M, pl, pr):
    global flag, target_idx, target_idx_limit

    pc = (pl + pr) // 2
    if sum(trees[pc+1:]) - range[pc]*(pr - pc) == M:
        flag = 1
        target_idx = pc
        return
    if pl > pr:
        flag = -1
        target_idx = pc
        target_idx_limit = pl
        return

    elif sum(trees[pc+1:]) - trees[pc]*(pr - pc) > M:
        bin_search(trees, M, pc + 1, pr)

    else:
        bin_search(trees, M, pl, pc - 1)

bin_search(trees, M, 0, len(trees) - 1)

if flag == 1:
    print(trees[target_idx])
else:
    candidate = range(trees[target_idx]+1, trees[target_idx_limit])
    bin_search(candidate, M, 0, len(candidate) -1)
    print(candidate[target_idx])
    

