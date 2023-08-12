N = int(input())

pos = [0] * N                   # 각 열에 배치한 퀸의 위치 ~ index: 열번호, element: 행번호 
flag_a = [False] * N            # 퀸을 배치한 행 체크 ~ 중복을 피하기 위해
flag_b = [False] * (2*N-1)      # 퀸을 배치한 대각선(상승방향) 체크
flag_c = [False] * (2*N-1)      # 퀸을 배치한 대각선(하강방향) 체크

cnt = 0

def set(i):
    global cnt
    '''i열의 알맞은 위치에 퀸을 배치'''
    for j in range(N):
        if (not flag_a[j]               # j행에 퀸이 배치되지 않았고
            and not flag_b[i+j]         # 대각선 상승 방향으로 퀸이 배치되지 않았고
            and not flag_c[i-j+N-1]):   # 대각선 하강 방향으로 퀸이 배치되지 않았다면,
            pos[i] = j      # 퀸을 j행에 배치
            if i == N-1:    # 0행부터 시작해서 N-1행까지 퀸 배치가 완료되었다면,
                cnt += 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] = True
                set(i+1)    # 다음 열에 퀸을 배치
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] = False

set(0) # 0열부터 퀸 배치 시작

print(cnt)