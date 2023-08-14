N = int(input())
A_list = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9



def operate(prev_list, order):
    global min_num
    global max_num

    if order == N-1:
        max_num = max(prev_list, max_num)
        min_num = min(prev_list, min_num)
        return
    
    
    
    for i in range(4):
        if operator[i] == 0:
            continue
        
        operator[i] -= 1

        if i == 0:
            operate(prev_list + A_list[order+1], order+1)
        elif i == 1:
            operate(prev_list - A_list[order+1], order+1)
        elif i == 2:
            operate(prev_list * A_list[order+1], order+1)
        else:
            operate(int(prev_list / A_list[order+1]), order+1)

        operator[i] += 1


        
    
operate(A_list[0], 0)
print(max_num)
print(min_num)