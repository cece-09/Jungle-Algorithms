n = int(input())
m = int(input())

print(n*(m%10))
print(n*((m//10)%10))
print(n*((m//100)))
print(n*m)

# m의 index 값을 곱하는 것도 좋은것 같다.
