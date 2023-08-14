# 가장 가까운 두 점
import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# x축 기준 정렬
graph.sort()


# 두 점 사이의 거리 계산 함수
def calc(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2


def dq(left, right):
    # 점 하나의 거리는 없으니 최대값 리턴
    if left == right:
        return float("inf")
    # 점이 두개 남으면 사이의 거리 리턴
    elif right - left == 1:
        return calc(graph[left], graph[right])
    # 분할
    mid = (left + right) // 2
    ans = min(dq(left, mid), dq(mid + 1, right))

    coor = []
    # x축 기준으로 후보 점들 찾기
    for i in range(left, right + 1):
        d = graph[i][0] - graph[mid][0]
        if d**2 < ans:
            coor.append(graph[i])

    # y축 기준 정렬
    coor.sort(key=lambda x: x[1])
    # y축 기준으로 후보 점들 사이의 거리 비교
    for i in range(len(coor) - 1):
        for j in range(i + 1, len(coor)):
            if (coor[i][1] - coor[j][1]) ** 2 < ans:
                ans = min(ans, calc(coor[i], coor[j]))
            else:
                break
            # 현재 후보 점이 다음 점과 최소 거리보다 머다면 더 볼 필요가 없음
            # 위 처리가 없으면 시간 초과 발생
    return ans


print(dq(0, n - 1))
