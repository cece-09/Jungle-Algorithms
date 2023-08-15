n, m = map(str, input().split())

n = n[-1] + n[1] + n[0]
m = m[-1] + m[1] + m[0]

if n > m:
    print(n)
else:
    print(m)

# num1, num2 = input().split()
# num1 = int(num1[::-1])  # [::-1] : 역순
# num2 = int(num2[::-1])

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)
