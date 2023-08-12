# 정렬 Sorting Problem

## O(N^2) 알고리즘

### Exchange Sort

### Insertion Sort

### Selection Sort

### Bubble Sort

```python

def bubble_sort():
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
```

## O(logN) 알고리즘

### Merge Sort

[병합 정렬의 merge 함수는 담당 범위보다 큰 연산을 하지 않는다.](https://www.acmicpc.net/board/view/109246)

### Quich Sort

### Heap Sort

### Decision Tree

## Sorting by Distribution

### Bucket Sort

### Radix Sort

### MSD Sort

### LSD Sort
