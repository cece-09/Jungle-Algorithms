numbering = 0

def make_Zs(n):
    global numbering

    # 종료 조건
    if n == 0:
        order = numbering
        numbering += 1
        return [[str(order)]]
    
    # Recursive Works
    sub_Zs_1 = make_Zs(n-1)
    sub_Zs_2 = make_Zs(n-1)
    sub_Zs_3 = make_Zs(n-1)
    sub_Zs_4 = make_Zs(n-1)
    output = []

    # 윗줄
    for i in range(len(sub_Zs_1)):
        output.append(sub_Zs_1[i] + sub_Zs_2[i])

    # 아랫줄
    for i in range(len(sub_Zs_3)):
        output.append(sub_Zs_3[i] + sub_Zs_4[i])

    return output

N, r, c = map(int, input().split())

# print('\n'.join(make_Zs(N)))

print(int(make_Zs(N)[r][c]))


'''

N = 1
**12
**34


N = 2
****
****
****
****

'''
