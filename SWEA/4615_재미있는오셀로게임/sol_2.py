import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 처음엔 가운데에 배치

    # 1은 흑돌
    # 2는 백돌
    arr = [[0]*N for _ in range(N)]
    lo = int(N / 2)
    # 초기값 설정
    arr[lo][lo], arr[lo-1][lo-1], arr[lo-1][lo], arr[lo][lo-1] = 2, 2, 1, 1

    # print(arr)

    # 상하좌우 대각선까지 모두 8방향 확인해야함
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 0, -1, 1]

    for i in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        arr[y][x] = color

        print(x, y, color)

        stack = []

        if color == 1:

            for j in range(8):
                # 만약 상하좌우 대각선에 상대방이 있으면,
                if 0 <= (y+dy[j]) <= N-1 and 0 <= (x+dx[j]) <= N-1:
                    if arr[y+dy[j]][x+dx[j]] == 2:
                        # 그 길로 쭉 따라서 내랑 같은 편이 있는지 확인한다.
                        stack.append((y+dy[j], x+dx[j]))
                        print('stack', stack)
                        while stack:
                            pp = stack.pop()
                            new_y = pp[0] + dy[j]

                            new_x = pp[1] + dx[j]
                            if 0 <= new_y <= N - 1 and 0 <= new_x <= N - 1:
                                if arr[new_y][new_x] == 2:

                                    stack.append((new_y, new_x))

                                else:
                                    if arr[new_y][new_x] == 1:
                                        arr[pp[0]][pp[1]] = 1


        elif color == 2:
            for j in range(8):
                # 만약 상하좌우 대각선에 상대방이 있으면,
                if 0 <= (y+dy[j]) <= N-1 and 0 <= (x+dx[j]) <= N-1:
                    if arr[y + dy[j]][x + dx[j]] == 1:
                        # 그 길로 쭉 따라서 내랑 같은 편이 있는지 확인한다.
                        stack.append((y + dy[j], x + dx[j]))

                        while stack:
                            pp = stack.pop()
                            new_y = pp[0] + dy[j]

                            new_x = pp[1] + dx[j]
                            if 0 <= new_y <= N - 1 and 0 <= new_x <= N - 1:
                                if arr[new_y][new_x] == 1:
                                    stack.append((new_y, new_x))

                                else:
                                    if arr[new_y][new_x] == 2:
                                        arr[pp[0]][pp[1]] = 2
        for i in arr:
            print(i)
    print(arr)
    # print(arr.count(1), arr.count(2))
