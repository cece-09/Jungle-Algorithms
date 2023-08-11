import sys
import itertools

input = sys.stdin.readline

n = int(input())
W_arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
# W_arr = []
# for i in range(n):
#     W_arr.append(list(map(int, input().split())))

a = [i for i in range(n)]
total_case = list(itertools.permutations(a, n))


def check_case(W_arr, case):
    case = case + (case[0],)
    cost = 0
    for i in range(len(case) - 1):
        if W_arr[case[i]][case[i + 1]] == 0:
            return int(10e9)  # min을 뽑아야 하니까
        cost += W_arr[case[i]][case[i + 1]]

    return cost


answer = int(10e9)
for case in total_case:
    answer = min(answer, check_case(W_arr, case))

print(answer)
