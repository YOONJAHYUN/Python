import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    def new(arr, a):
        while a != 4:

            new_arr = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    new_arr[i][j] = arr[n - j - 1][i]

            for i in range(n):
                print(''.join(map(str, new_arr[i])))

            return new(new_arr, a+1)



    print(f'#{tc}')
    new(arr, 1)

