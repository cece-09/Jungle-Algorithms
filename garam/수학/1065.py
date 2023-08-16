x = input()
cnt = 0
for i in range(1, int(x) + 1):
    if i < 100:
        cnt += 1
    elif i >= 100:
        i = str(i)
        if int(i[2]) - int(i[1]) == int(i[1]) - int(i[0]):
            cnt += 1
print(cnt)
