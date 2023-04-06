import sys
sys.stdin = open('input.txt')

def dessert(y, x, ans, dir):
    global result, i, j

    # 다시되돌아왔을때 종료
    # 이때 마지막 방향이여야 함
    if y == i and x == j and dir == 3:
        result = max(result, len(ans))
        return

    if 0 <= x < N and 0 <= y < N and data[y][x] not in ans:
        path = ans + [data[y][x]]

        # 대각선으로 이동시
        ny = y + direction[dir][0]
        nx = x + direction[dir][1]
        dessert(ny, nx, path, dir)

        # 꺾는 경우 포함
        if dir < 3:
            ny = y + direction[dir+1][0]
            nx = x + direction[dir+1][1]
            dessert(ny, nx, path, dir+1)
        


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    result = -1
    for i in range(N):
        for j in range(N):
            dessert(i, j, [], 0)

    print(f'#{tc}', result)