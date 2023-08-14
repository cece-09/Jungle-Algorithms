N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0

def sol(target):
    global white_cnt, blue_cnt

    color_set = []
    k = 0
    element = 0
    for i in range(len(target)):
        if len(set(target[i])) > 1:
            break
        if 1 in set(target[i]):
            element = 1
        else:
            element = 0
        color_set.append(element)
        if len(set(color_set)) > 1:
            break
        k += 1
    
    if k == len(target):
        if 1 in set(color_set):
            blue_cnt += 1
        else:
            white_cnt += 1
        return

    # 1사분면
    sol([x[:len(papers)//2] for x in papers[:len(papers)//2]])
        
    # 2사분면
    sol([x[len(papers)//2:] for x in papers[:len(papers)//2]])

    # 3사분면
    sol([x[:len(papers)//2] for x in papers[len(papers)//2:]])

    # 4사분면
    sol([x[len(papers)//2:] for x in papers[len(papers)//2:]])

sol(papers)
print(white_cnt)
print(blue_cnt)