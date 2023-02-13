
def triangle(n, depth, arr):
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 1

    while n <= depth:
        for i in range(n):
            if i >= 1:
                arr[n][i] = arr[n-1][i] + arr[n-1][i-1]
            else:
                arr[n][i] = arr[n-1][i]

    return triangle(n, depth + 1, arr)


T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    n = int(input())
    print(triangle(n, 1))