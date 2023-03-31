import sys

sys.stdin = open('input.txt')

def hamburger(i, n, cal, taste):
    global ans

    if i == n:
        if cal<=L:
            ans = max(ans, taste)
            return

    if cal > L:
        return

    hamburger(i+1, n, cal+data[i][1], taste+data[i][0])
    hamburger(i+1, n, cal, taste)


T = int(input())
for tc in range(1, T+1):
    # N 재료의 수, L 제한 칼로리
    N, L = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    hamburger(0, N, 0, 0)
    print(f'#{tc}', ans)
