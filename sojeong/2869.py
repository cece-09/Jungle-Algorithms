A, B, V = map(int, input().split())

O = A - B
print((V-A) // O + ((V-A) % O != 0) + 1)
