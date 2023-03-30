import sys

sys.stdin = open('input.txt')

def low_cost(depth, n, cost):
    global selection, ans

    if depth == n:
        ans = min(ans, cost)
        return

    if cost >= ans:
        return

    for i in range(n):
        if not selection[i]:
            selection[i] = True
            low_cost(depth+1, n, cost+V[depth][i])
            selection[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    selection = [False] * N
    ans = 100 * N
    low_cost(0, N, 0)
    print(f'#{tc}', ans)
