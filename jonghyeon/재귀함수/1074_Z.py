N, r, c = map(int, input().split())


def down_scale(N, r, c, answer):

    if N == 0:
        print(answer)
        return

    N -= 1

    # 1사분면
    if r < 2 ** N and c < 2 ** N:
        answer += ( 2 ** N ) * ( 2 ** N ) * 0

    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        answer += ( 2 ** N ) * ( 2 ** N ) * 1
        c -= ( 2 ** N )

    # 3사분면    
    elif r >= 2 ** N and c < 2 ** N: 
        answer += ( 2 ** N ) * ( 2 ** N ) * 2
        r -= ( 2 ** N )

    # 4사분면    
    else:
        answer += ( 2 ** N ) * ( 2 ** N ) * 3
        r -= ( 2 ** N )
        c -= ( 2 ** N )

    down_scale(N, r, c, answer)


down_scale(N, r, c, 0)