import sys

sys.stdin = open('input.txt')

def make_number(i, j, depth, ans):
    global cnt, result
    if depth == 6:
        if ans not in result:
            cnt += 1
            result.append(ans)
        return



    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = i + di, j + dj

        if 0 <= ni < 4 and 0 <= nj < 4:
            make_number(ni, nj, depth+1, ans+data[ni][nj])

T = int(input())

for tc in range(1, 1+T):
    data = [list(map(str, input().split())) for _ in range(4)]
    cnt = 0
    result = []

    for i in range(4):
        for j in range(4):
            make_number(i, j, 0, data[i][j])
    print(f'#{tc}', cnt)

