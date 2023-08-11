# 정렬
n = int(input())
m = []
temp = 0
for i in range(n):
    m.append(int(input()))
# print(m)
for i in range(0, n):
    for j in range(1, n):
        if m[j] < m[j - 1]:
            temp = m[j - 1]
            m[j - 1] = m[j]
            m[j] = temp
            # print("m",[j],m[j])
for i in range(0, n):
    print(m[i])

# 위 방법은 라이브러리 안쓴 하드코딩

