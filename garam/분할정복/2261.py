# 가장 가까운 두 점
import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 중복 가능(같은 좌표를 가질 수 있음)
# 첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력
