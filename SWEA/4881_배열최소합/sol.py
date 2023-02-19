import sys

sys.stdin = open('input.txt')

def f(mat, N, depth, sum):
    global result, ans
    global index

    if N == depth:
        ans = min(ans, sum)
        return

    for i in range(N):
        if index[i] == True:
            continue



        index[i] = True
        f(mat, N, depth+1, mat[depth][i] + sum)
        index[i] = False



    return ans


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    index = [False for _ in range(N + 1)]


    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = N * 9
    f(mat, N, 0, 0)
    print(f'#{tc}', ans)