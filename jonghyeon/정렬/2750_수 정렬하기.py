#Bubble Sort
N = int(input())

unsorted = []
for _ in range(N):
    unsorted.append(int(input()))

# print("정렬 전:",unsorted)

for i in range(N-1,0,-1): # i : 어디까지 검사하는가?
    for j in range(i): # j : 버블의 위치
        if unsorted[j] > unsorted[j+1]: # 버블 왼쪽값 > 버블 오른쪽 => 역전상태!
            unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]

## Time Complexity :  O(n^2)
# print("정렬 후:",unsorted)

for i in range(N):
    print(unsorted[i])