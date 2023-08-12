N = int(input())
cnt = 0
process = []
def hanoi_move(x, y, num_tower):
    global cnt
    # if num_tower == 1:
    #     cnt += 1
    #     if N <= 20:
    #         process.append(str(x) + ' ' + str(y))
    #     return
    if num_tower > 1:
        hanoi_move(x, 6 - (x + y), num_tower - 1)

    cnt += 1
    if N <= 20:
        process.append(str(x) + ' ' + str(y))

    if num_tower > 1:
        hanoi_move(6 - (x + y), y, num_tower - 1)

hanoi_move(1, 3, N)
print(cnt)
if N <= 20:
    for i in range(len(process)):
        print(process[i])