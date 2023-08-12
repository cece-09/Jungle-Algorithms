def hanoi_move(x, y, num_tower):
    if num_tower == 1:
        print(x, y, sep = ' ')
        return
    
    hanoi_move(x, 6 - (x + y), num_tower - 1)
    print(x, y, sep = ' ')
    hanoi_move(6 - (x + y), y, num_tower - 1)

N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi_move(1, 3, N)