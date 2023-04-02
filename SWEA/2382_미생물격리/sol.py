import sys
sys.stdin = open('input.txt')

def suwan(start, end):
    global arr, data

    if start == end:
        return

    for i in arr:
        print(*i)
    print('####'*20)

    new_data = []
    # data에 저장된 좌표를 꺼낸다.

    for y, x in data:
        print(y, x)
        num, move = arr[y][x]

        # move가 상(1)이라면
        if move == 1:
            # 옮기기전에 원래 자리를 0 으로 만든다.
            arr[y][x] = [0,0]

            # y를 한 칸 옮긴다.
            y -= 1

            # 옮겼는데 약품이 처리된 구간이면
            if y == 0:
                # 군집이 타노스
                num //= 2
                # 방향전환
                move = 2

            # 옮길 자리에 다른 군집이 올라칸다?
            if (0 <= x-1 < N and arr[y][x-1][1] == 4) or (0 <= x+1 < N and arr[y][x+1][1] == 3) or (0 <= y+1 < N and arr[y+1][x][1] == 2) or (0 <= y-1 < N and arr[y-1][x][1] == 1) or arr[y][x]:
                # 미생물 수를 늘리기
                # arr[y][x][0] += num
                # 이동방향 변경
                temp = move
                temp_num = num
                for n, moving in (arr[y][x-1], arr[y][x+1], arr[y+1][x], arr[y-1][x], arr[y][x]):
                    if temp_num < n:
                        temp_num = n
                        temp = moving

                arr[y][x][0] += num
                arr[y][x][1] = temp

            else:

                # 모든 처리가 끝났으므로 arr에 다시 값 넣어주기
                arr[y][x][0] += num

                arr[y][x][1] = move

            for i in arr:
                print(*i)
            print('####' * 20)

        # 방향이 하 인경우
        elif move == 2:
            # 옮기기전에 원래 자리를 0 으로 만든다.
            arr[y][x] = [0,0]

            # y를 한 칸 옮긴다.
            y += 1

            # 옮겼는데 약품이 처리된 구간이면
            if y == N - 1:
                # 군집이 타노스
                num //= 2
                move = 1

            # 옮길 자리에 다른 군집이 올라칸다?
            if (0 <= x - 1 < N and arr[y][x - 1][1] == 4) or (0 <= x + 1 < N and arr[y][x + 1][1] == 3) or (
                    0 <= y + 1 < N and arr[y + 1][x][1] == 2) or (0 <= y - 1 < N and arr[y - 1][x][1] == 1) or arr[y][x]:
                # 미생물 수를 늘리기
                # arr[y][x][0] += num
                # 이동방향 변경
                temp = move
                temp_num = num
                for n, moving in (arr[y][x - 1], arr[y][x + 1], arr[y + 1][x], arr[y - 1][x], arr[y][x]):
                    if temp_num < n:
                        temp = moving
                        temp_num = n
                arr[y][x][0] += num
                arr[y][x][1] = temp
            else:

                # 모든 처리가 끝났으므로 arr에 다시 값 넣어주기
                arr[y][x][0] += num
                arr[y][x][1] = move

            for i in arr:
                print(*i)
            print('####' * 20)

        # 방향이 좌 인경우
        elif move == 3:
            # 옮기기전에 원래 자리를 0 으로 만든다.
            arr[y][x] = [0,0]

            # x를 한 칸 옮긴다.
            x -= 1

            # 옮겼는데 약품이 처리된 구간이면
            if x == 0:
                # 군집이 타노스
                num //= 2
                move = 4

            # 옮길 자리에 다른 군집이 올라칸다?
            if (0 <= x - 1 < N and arr[y][x - 1][1] == 4) or (0 <= x + 1 < N and arr[y][x + 1][1] == 3) or (
                    0 <= y + 1 < N and arr[y + 1][x][1] == 2) or (0 <= y - 1 < N and arr[y - 1][x][1] == 1) or arr[y][x]:
                # 미생물 수를 늘리기
                # arr[y][x][0] += num
                # 이동방향 변경
                temp = move
                temp_num = num
                for n, moving in (arr[y][x - 1], arr[y][x + 1], arr[y + 1][x], arr[y - 1][x], arr[y][x]):
                    if temp_num < n:
                        temp = moving
                        temp_num = n

                arr[y][x][0] += num
                arr[y][x][1] = temp

            else:
                # 모든 처리가 끝났으므로 arr에 다시 값 넣어주기
                arr[y][x][0] += num
                arr[y][x][1] = move

            for i in arr:
                print(*i)
            print('####' * 20)

        # 방향이 우 인경우
        else:
            # 옮기기전에 원래 자리를 0 으로 만든다.
            arr[y][x] = [0,0]

            # x를 한 칸 옮긴다.
            x += 1

            # 옮겼는데 약품이 처리된 구간이면
            if x == N-1:
                # 군집이 타노스
                num //=2
                move = 3

            # 옮길 자리에 다른 군집이 올라칸다?
            if (0 <= x - 1 < N and arr[y][x - 1][1] == 4) or (0 <= x + 1 < N and arr[y][x + 1][1] == 3) or (
                    0 <= y + 1 < N and arr[y + 1][x][1] == 2) or (0 <= y - 1 < N and arr[y - 1][x][1] == 1) or arr[y][x]:
                # 미생물 수를 늘리기
                # arr[y][x][0] += num
                # 이동방향 변경
                temp = move
                temp_num = num
                for n, moving in (arr[y][x - 1], arr[y][x + 1], arr[y + 1][x], arr[y - 1][x], arr[y][x]):
                    if temp_num < n:
                        temp = moving
                        temp_num = n

                arr[y][x][0] += num
                arr[y][x][1] = temp
            else:
                # 모든 처리가 끝났으므로 arr에 다시 값 넣어주기
                arr[y][x][0] += num
                arr[y][x][1] = move


            for i in arr:
                print(*i)
            print('####' * 20)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(data)
    # suwan(start+1, end)




T = int(input())

for tc in range(1, T+1):

    # N 셀의 개수, M 격리기간, K 미생물 군집의 개수
    N, M, K = map(int, input().split())
    arr = [[[0, 0] for _ in range(N)] for _ in range(N)]
    # for i in arr:
    #     print(i)
    data = []
    # print(arr)



    # 세로위치, 가로위치, 미생물 수 , 이동방향(상 1 하 2 좌 3 우 4)
    for _ in range(K):
        y, x, num, move = map(int, input().split())
        arr[y][x] = [num, move]
        data.append([y, x])

    suwan(0, M)

    # for i in arr:
    #     print(*i)
    # print(f'#{tc}', sum(arr))
