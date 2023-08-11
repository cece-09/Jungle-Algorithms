# WEEK-01 Algorithms

## DAY2

2023-08-11
수학~ 범위부터 메모

### 소수의 판별

[1978] [9020]
N보다 작은 수 k 에 대해 N % k 를 검사한다

- k 반복문의 범위를 math.sqrt(N, 2) 즉 제곱근으로 제한할 수 있다.
- <https://freedeveloper.tistory.com/391>
  에라토네스의 체를 사용한다
- 케이스가 많은 경우 유용함

### 재귀 Recursion

[야너두 재귀할수있어..](https://velog.io/@eddy_song/you-can-solve-recursion)

[1914] 하노이 탑

[9663] N Queens
카드 놓기와 유사한 (모든 경우의 수를 탐색하는) 방법으로 풀 수 있을 것이라고 생각해서 대략 다음과 같은 방식으로 코드를 작성했다.

```python
def queen(N):
  if N이 마지막:
      카운트하고 리턴
  모든 열에 대해:
    공격 가능할 경우:
      이 열에 퀸을 놓고
      queen(N+1)
```

[공격가능여부를 체크하는 방법]
정상적으로 답을 내었으나, 계속 시간 초과가 떴다. 문제는 아래, 대각선이 아닌 경우, 즉 퀸의 공격가능여부를 판단하는 부분을 잘못 구현한 것이었다. `cols` 배열에 각 행에 놓아진 퀸 인덱스를 저장해두고, `q`행 `i`열의 공격가능여부를 판단할 때 배열을 모두 탐색한다.

```python
def attackable(i, q):
    for r, col in enumerate(cols):
        if col == None:
            continue
        if col == i:
            return True
        if abs(col-i) == abs(q-r):
            return True
    return False
```

배열을 모두 탐색하면 기본 재귀에 걸리는 N*N에 다시*N 을 하여 무려 N의 세제곱 타임이 걸리게 된다.

[공격가능여부를 미리 flag 처리하는 방법]

```python
def queen(N):
  if N이 마지막:
      카운트하고 리턴
  모든 열에 대해:
    공격 가능할 경우:
      이 열에 퀸을 놓고, 다음 행들에 대해 미리 대각선, 아래를 flag처리
      queen(N+1)
      flag 해제
```

다음으로 생각했던 것은, 2차원 배열을 놓고, N행의 퀸 위치를 선택할 때 마다 미리 퀸을 놓을 수 없는 위치를 flage처리하여 다음 반복 떄 건너뛰도록 하는 방법이다. 그러나 이 역시 flag처리 과정에서 N번 반복문을 사용하여, 세제곱 시간이 걸리는 것은 동일했다. (오히려 2차원 배열로 인해 메모리 사용량이 늘었다.)

[최종 완성 코드]

```python
# n = 보드 가로세로, 퀸의 수
# i = 현재 놓은 퀸의 수
# a = 퀸 좌표의 열 인덱스
# b = 퀸 좌표의 오른쪽 대각선 열 인덱스
# c = 퀸 좌표의 왼쪽 대각선 열 인덱스
def queens(n, i, a, b, c):
    global cnt
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        cnt += 1
        return


N = int(input())
cnt = 0
queens(N, 0, [], [], [])
print(cnt)
```

위키피디아 파이썬 코드를 보고 작성했다. 흐름 자체는 유사하나 구현에서 flag보다 리스트에 추가하여 in으로 검사하는 부분이 큰 차이다. in 에 대해서는, 막연히 선형탐색 (for문) 과 같다고 생각하여, 탐색을 직접 구현하면서 더 이상 탐색할 필요가 없는 예외상황을 처리해주는 것이 더 빠르다고 생각했으나, **파이썬 내부의 최적화로 인해 in의 작동이 매우 빠르다고 한다.** 실제로 실행 시간을 재어 보니 N=15인 경우 3배 이상 차이가 발생했다.

알고리즘 상의 문제는, flag처리를 할 경우 unflag도 생각해야 한다는 것이다. 그래서 불필요하게 길고 복잡한 코드를 작성하지 않았나 싶다. 알고리즘을 풀 때는 1. 가급적 깔끔하게 2. 로직에만 집중하여 코드를 짜자.
