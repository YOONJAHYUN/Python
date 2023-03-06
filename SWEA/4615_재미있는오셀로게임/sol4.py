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
        # 흑돌일 때
        if color == 1:
            # 각방향으로 순회함
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)):
                # 오셀로 판 안에 있는 경우
                if 0 <= x + dx - 1 < N and 0 <= y + dy - 1 < N:
                    # 가다가 백돌이 있음
                    if arr[y + dy - 1][x + dx - 1] == 2:
                        # 그 방향으로 쭈욱 찾아줌
                        for mul in range(1, N):
                            nx, ny = x + dx * mul - 1, y + dy * mul - 1
                            # 그방향으로 쭉 찾을때
                            if 0 <= nx < N and 0 <= ny < N:
                                # 2라면 계속 찾음
                                if arr[ny][nx] == 2:
                                    continue
                                # 2가 아니라면?
                                else:
                                    # 만약 0이면 오셀로가 뒤집어지지않음
                                    if arr[ny][nx] == 0:
                                        break
                                    # 만약 1이라면 오셀로가 뒤집어져야함
                                    else:
                                        # 2로 찾은 부분 다 뒤집어주기
                                        for minus in range(0, mul):
                                            arr[ny-dy*minus][nx-dx*minus] = 1
                                        break

                            # 방향 나가면? 그냥 중지 어짜피 안뒤집어져야됨
                            else:
                                break
        # 백돌일 때
        elif color == 2:
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)):

                if 0 <= x + dx - 1 < N and 0 <= y + dy - 1 < N:
                    if arr[y + dy - 1][x + dx - 1] == 1:

                        for mul in range(1, N):
                            nx, ny = x + dx * mul - 1, y + dy * mul - 1

                            if 0 <= nx < N and 0 <= ny < N:
                                if arr[ny][nx] == 1:

                                    continue
                                else:

                                    if arr[ny][nx] == 0:
                                        break

                                    else:
                                        for minus in range(0, mul):
                                            arr[ny - dy * minus][nx - dx * minus] = 2
                                        break

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