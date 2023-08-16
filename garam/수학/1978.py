n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for a in arr:
    for j in range(2, a+1):
        if (j == a):
            cnt +=1
        elif (a % j == 0):
            break       
                

print(cnt)