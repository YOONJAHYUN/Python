import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(input().rstrip()) for _ in range(N)]
    # print(data)

    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    result = 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            if data[i][j] == 'o':
                cnt += 1

                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]

                    if 0 <= nx < N and 0 <= ny < N:
                        if data[ny][nx] == 'o':

                            while True:
                                if 0 <= nx < N and 0 <= ny < N:
                                    if data[ny][nx] == 'o':
                                        nx = nx + dx[k]
                                        ny = ny + dy[k]
                                        cnt += 1
                                    else:
                                        if cnt >= 5:
                                            result = 1
                                        else:
                                            cnt = 1
                                        break
                                else:
                                    if cnt >= 5:
                                        result = 1
                                    else:
                                        cnt = 1
                                    break

                if cnt >= 5:
                    result = 1
                    print(f'#{tc}', 'YES')
                    break

    else:
        if result == 0:
            print(f'#{tc}', 'NO')