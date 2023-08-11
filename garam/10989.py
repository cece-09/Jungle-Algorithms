import sys

input = sys.stdin.readline

num = int(input())
numbers = [0] * 10001
# print(numbers)
for i in range(num):
    numbers[int(input())] += 1
    # print(numbers)
for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)

# 0으로 집합을 만들고 인덱스 해당 부분을 +1을줘서 인덱스를 출력하면됨
