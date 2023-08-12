import sys

input = sys.stdin.readline

num = int(input())
numbers = [0] * 11
# print(numbers)
for i in range(num):
    numbers[int(input())] += 1
    # print(numbers)
    # print(numbers[i])
for i in range(11):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            # print(numbers[i])
            # print(range(numbers[i]))
            print(i)

# 0으로 집합을 만들고 인덱스 해당 부분을 +1을줘서 인덱스를 출력하면됨
