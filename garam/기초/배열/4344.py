c = int(input())
# 이 for 문을 한번 돌렸을 때 출력까지 뽑아버림
for i in range(c):
    a = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for j in range(1, len(a)):
        sum += a[j]
    avg = sum / (len(a) - 1)
    for j in range(1, len(a)):
        if a[j] > avg:
            cnt += 1
    result = (cnt / a[0]) * 100
    print("%.3f" %result + "%")

