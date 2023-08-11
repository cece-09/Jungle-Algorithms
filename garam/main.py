N = input()

# 1자리수 한수 총 개수: 9
# 2자리수 한수 총 개수: 90
# 3자리수 한수 총 개수: 45

if len(N) == 1:
    print(int(N))
elif len(N) == 2:
    print(int(N))
elif len(N) == 3:

    three_han = []
    for x in range(1, int(N[0])+1):
        three_han.append(int(str(x)*3))
        for j in range(1, 5):
            if (x - j) > 0 and (x - 2*j) >= 0:
                han_num = int(str(x) + str(x-j) + str(x-2*j))
                three_han.append(han_num)
            if (x + j) < 9 and  (x + 2*j) <= 9:
                han_num = int(str(x) + str(x+j) + str(x+2*j))
                three_han.append(han_num)
    three_han.sort()
    
    cnt = 99
    for n in three_han:
        if n <= int(N) :
            cnt += 1
        else:
            break
    print(cnt)
else:
    print(144)