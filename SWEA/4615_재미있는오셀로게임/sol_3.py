import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0]*N for _ in range(N)]

    # 기본 틀 만들기
    arr[N//2][N//2], arr[N//2 - 1][N//2], arr[N//2][N//2 - 1], arr[N//2 - 1][N//2 - 1] = 2, 1, 1, 2
    # print(arr)
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]

    # color 1 흑돌 2백돌
    for _ in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        arr[y][x] = color

        for i in range(8):

            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:


                if color == 1:
                    # 만약 대각선, 상하좌우에서 2를 찾았으면
                    # stack에 넣어준다.
                    stack = []
                    if arr[ny][nx] == 2:
                        # 그 다음번에도 2일 수 있다.
                        # 그러면, 1을 찾을때까지 다 스택에 넣자.
                        cnt = 0

                        while 0<= nx+dx[i]*cnt<N and 0<= ny+dy[i]*cnt< N:
                            if arr[ny + dy[i]*cnt][nx + cnt * dx[i]] == 2:
                                stack.append((ny + dy[i] * cnt, nx + cnt * dx[i]))
                                cnt += 1
                            elif arr[ny + dy[i]*cnt][nx + cnt* dx[i]] == 1:
                                while stack:
                                    a, b = stack.pop()
                                    arr[a][b] = 1
                                break
                            else:
                                break
                elif color == 2:
                    # 만약 대각선, 상하좌우에서 2를 찾았으면
                    # stack에 넣어준다.
                    stack = []
                    if arr[ny][nx] == 1:
                        # 그 다음번에도 2일 수 있다.
                        # 그러면, 1을 찾을때까지 다 스택에 넣자.
                        cnt = 0
                        while 0 <= nx + dx[i] * cnt < N and 0 <= ny + dy[i] * cnt < N:
                            if arr[ny + dy[i] * cnt][nx + cnt * dx[i]] == 1:
                                stack.append((ny + dy[i] * cnt, nx + cnt * dx[i]))
                                cnt += 1
                            elif arr[ny + dy[i] * cnt][nx + cnt * dx[i]] == 2:
                                while stack:
                                    a, b = stack.pop()
                                    arr[a][b] = 2
                                break
                            else:
                                break
    count1=0
    count2 = 0
    for i in arr:
        count1 += i.count(1)
        count2 += i.count(2)
    print(f'#{tc}', count1, count2)
