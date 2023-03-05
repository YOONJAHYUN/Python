import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 초기설정
    arr = [[0]*N for _ in range(N)]

    arr[N//2][N//2], arr[N//2-1][N//2-1], arr[N//2-1][N//2], arr[N//2][N//2-1] = 2, 2, 1, 1

    # for i in arr:
    #     print(i)
    # print()

    # 1 흑돌 2 백돌
    for _ in range(M):
        x, y, color = map(int, input().split())
        arr[y-1][x-1] = color

        if color == 1:
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)):

                if 0 <= x + dx - 1 < N and 0 <= y + dy - 1 < N:
                    if arr[y + dy - 1][x + dx - 1] == 2:
                        # arr[y + dy - 1][x + dx - 1] = 1
                        for mul in range(1, N):
                            nx, ny = x + dx * mul - 1, y + dy * mul - 1

                            if 0 <= nx < N and 0 <= ny < N:
                                if arr[ny][nx] == 2:
                                    # arr[ny][nx] = 1
                                    pass
                                else:

                                    if arr[ny][nx] == 0:
                                        # for minus in range(1, mul):
                                        #     arr[ny-dy*minus][nx-dx*minus] = 2
                                        pass
                                    else:
                                        for minus in range(0, mul):
                                            arr[ny-dy*minus][nx-dx*minus] = 1

                            else:
                                break
        elif color == 2:
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)):

                if 0 <= x + dx - 1 < N and 0 <= y + dy - 1 < N:
                    if arr[y + dy - 1][x + dx - 1] == 1:
                        # arr[y + dy - 1][x + dx - 1] = 2
                        for mul in range(1, N):
                            nx, ny = x + dx * mul - 1, y + dy * mul - 1

                            if 0 <= nx < N and 0 <= ny < N:
                                if arr[ny][nx] == 1:
                                    # arr[ny][nx] = 2
                                    pass
                                else:

                                    if arr[ny][nx] == 0:
                                        pass
                                        # for minus in range(1, mul):
                                        #     arr[ny - dy * minus][nx - dx * minus] = 1
                                    else:
                                        for minus in range(0, mul):
                                            arr[ny - dy * minus][nx - dx * minus] = 2

                            else:
                                break

        for i in arr:
            print(i)
        print()
    count1=0
    count2=0
    for i in arr:
        count1 += i.count(1)
        count2 += i.count(2)


    print(f'#{tc}', count1, count2)