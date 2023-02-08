import sys

sys.stdin = open('input.txt')


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input().rstrip()) for _ in range(N)]

    for i in range(N-1):
        for j in range(N-1):
            if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1]:
                print(f'#{tc+1}', 'yes')

    else:
        print(f'#{tc+1}', 'no')