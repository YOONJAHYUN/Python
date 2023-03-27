import sys
sys.stdin = open('input.txt')

T = int(input())

def cart(depth, i, n):

    if depth == n:
        return

    for i in range(n):
        if not selection[i]:



for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)
    cart(0, 0, N)
    selection = [False] * (N+1)


