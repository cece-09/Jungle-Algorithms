n, c = map(int, input().split())

array = [int(input()) for _ in range(n)]
array.sort()

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid    # 여차하면 지금 mid값도 나쁘지 않으므로 여기에서 기록
        else:
            end = mid - 1

start, end = 1, array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)