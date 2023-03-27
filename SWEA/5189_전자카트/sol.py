import sys
sys.stdin = open('input.txt')

T = int(input())

def cart(depth, ans, idx, n):
    global my_min, rsl

    if depth == n:
        my_min = min(my_min, ans)
        return

    for i in range(n):
        if not selection1[i] and not selection2[idx] and idx != i:
            selection1[i], selection2[idx] = True, True
            cart(depth+1, ans+data[idx][i], i, n)
            selection1[i], selection2[idx] = False, False


for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    selection1 = [False] * (N+1)
    selection2 = [False] * (N+1)


    my_min = 1e10
    cart(0, 0, 0, N)
    print(f'#{tc}', my_min)

