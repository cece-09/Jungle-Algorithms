N = int(input())


def visit(n, x1, y1, x2, y2):
    if n == 2:
        print(x1, y1, x2, y2)
        return
    visit(n//2, x1, y1, n//2, n//2)
    visit(n//2, n//2+1, y1, n, n//2)
    visit(n//2, x1, n//2+1, n//2, n)
    visit(n//2, n//2+1, n//2+1, n, n)


arr = 2 ** N
visit(arr, 1, 1, arr, arr)
