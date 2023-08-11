A, B, V = map(int, input().split())

day_cnt = 0

if (V - A) % (A-B) == 0:
    day_cnt = (V - A) // (A-B) + 1

else:
    day_cnt = (V - A) // (A-B) + 2

    
print(day_cnt)