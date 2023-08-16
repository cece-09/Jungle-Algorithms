T = int(input())
n = list(int(input()) for _ in range(T))


def is_prime(a):
    if a == 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


for i in n:
    temp = i // 2

    while temp > 0:
        if is_prime(temp):
            if is_prime(i - temp):
                print(temp, i - temp)
            break
        temp -= 1
