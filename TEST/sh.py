import sys

sys.stdin = open('input2.txt')

def eat(x, y, have, D, data):
    global yummy
    if D == 3:
        yummy += have
        return

    for k in range(4):
        for mul in range(1, N):
            nx = x + dx[k]*mul
            ny = y + dy[k]*mul

            # 주위에 다른 장기 알이 있다면,
            if 0 <= nx < N and 0 <= ny < N and data[ny][nx] == 1:
                # 그 옆에 공간이 있는지 체크한다.
                for plus in range(mul+1, N):
                    sx = x + dx[k] * plus
                    sy = y + dy[k] * plus
                    if 0 <= sx < N and 0 <= sy < N:
                        # 포가 위치 할 수 있다면 다시 새 함수 불러옴
                        if data[sy][sx] == 0:
                            eat(sx, sy, have+0, D+1, data)

                        # 다른 알이 있어서 포가 그 장기 알을 먹을 수 있다면, 그 또한 새함수 호출
                        elif data[sy][sx] == 1:
                            data[sy][sx] = 0
                            eat(sx, sy, have+1, D+1, data)

                    else:
                        # 공간을 벗어나면 걍 break
                        break

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, -1]
    dy = [1, -1, 0, 1]

    yummy = 0
    # 포의 위치
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = j, i
                data[y][x] = 0
                eat(x, y, 0, 0,data)

                break

    print(f'#{tc}', yummy)

