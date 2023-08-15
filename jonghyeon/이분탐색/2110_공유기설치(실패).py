import sys
input = sys.stdin.readline

'''
공유기를 설치할 거리를 이분 탐색으로 결정
'''

n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

max_diff = house[-1] - house[0]
start, end = 1, max_diff    # 집 사이의 최소 거리, 최대 거리
answer = 0

while start <= end:
    mid = (start + end) // 2 # 현재 '기준간격'
    print(start, end, mid)
    current = house[0] # 현재 '기준집 위치' (마지막으로 설치된 공유기 위치)
    count = 1 # 공유기 설치 개수
    diff = max_diff

    for i in range(1, n):
        if house[i] - current >= mid: # 간격이 mid 보다 넓으면 공유기 설치
            diff = min(diff, house[i] - current)
            count += 1
            current = house[i] # 공유기를 설치

    if count >= c: # 공유기 모두 설치 가능, 간격 늘림
        start = mid + 1
        answer = max(answer, diff)
    else: # 공유가 모두 설치 불가, 간격 좁힘
        end = mid - 1
    print(f'count: {count}')

print(answer)