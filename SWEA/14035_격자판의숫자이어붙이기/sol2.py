import sys

sys.stdin = open('input.txt')

def make_number(i, j, depth, ans):
    global visited
    if depth == 6:
        if (depth, i, j, ans) not in visited:
            visited[(depth, i, j, ans)] = 1
            result.append(ans)
        return

    if (depth, i, j, ans) in visited:
        return
    else:
        visited[(depth, i, j, ans)] = 1
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj

            if 0 <= ni < 4 and 0 <= nj < 4:
                make_number(ni, nj, depth+1, ans+data[ni][nj])


T = int(input())

for tc in range(1, 1+T):
    data = [list(map(str, input().split())) for _ in range(4)]
    result = []
    # visited에다가 해당까지 온 값과 i,j값을 넣어준다.
    visited = {}

    # print(visited)
    for i in range(4):
        for j in range(4):
            make_number(i, j, 0, data[i][j])
    result = set(result)
    print(f'#{tc}', len(result))



