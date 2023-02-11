import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    y, x = 99, arr[99].index(2)

    while y != 0:
        if x == 0:
            if arr[y][x+1] == 1:
                arr[y][x] = 0
                x = x + 1
            else:
                arr[y][x] = 0
                y = y - 1

        if x == 99:
            if arr[y][x-1] == 1:
                arr[y][x] = 0
                x = x - 1
            else:
                arr[y][x] = 0
                y = y - 1

        if 0 < x < 99:
            if arr[y][x+1] == 1:
                arr[y][x] = 0
                x = x + 1
            elif arr[y][x-1] == 1:
                arr[y][x] = 0
                x = x - 1
            else:
                arr[y][x] = 0
                y = y - 1

    print(f'#{tc}', x)




