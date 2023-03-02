import sys
import copy
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    # 시작점 찾기
    start_point = []
    result = 100*100
    min_start = 0
    for i in range(100):
        if data[0][i] == 1:
            start_point.append(i)

    # print(start_point)

    # 시작점에서 출발하여 사다리 끝까지 내려가본다.
    for start in start_point:
        # print(start)
        x = start
        y = 0
        my_data = copy.deepcopy(data)
        cnt = 0
        while True:

            if x == 0:
                if 0 <= y < 100 and 0 <= x+1 < 100 and my_data[y][x+1] == 1:
                    my_data[y][x] = 0
                    y = y
                    x = x + 1

                else:
                    if 0 <= y+1 < 100 and 0 <= x < 100:
                        my_data[y][x] = 0
                        y = y+1
                        x = x
                        # my_data[y+1][x] = 0
                cnt += 1

            elif x == 99:
                if 0 <= y < 100 and 0 <= x-1 < 100 and my_data[y][x-1] == 1:
                    my_data[y][x] = 0
                    y = y
                    x = x - 1
                    # my_data[y][x-1] = 0
                else:
                    if 0 <= y+1 < 100 and 0 <= x < 100:
                        my_data[y][x] = 0
                        y = y+1
                        x = x
                        # my_data[y + 1][x] = 0
                cnt += 1

            else:
                if 0 <= y < 100 and 0 <= x-1 < 100 and my_data[y][x - 1] == 1:
                    my_data[y][x] = 0
                    y = y
                    x = x - 1
                    # my_data[y][x-1] = 0
                elif 0 <= y < 100 and 0 <= x+1 < 100 and my_data[y][x + 1] == 1:
                    my_data[y][x] = 0
                    y = y
                    x = x + 1
                    # my_data[y][x + 1] = 0
                else:
                    if 0 <= y+1 < 100 and 0 <= x < 100:
                        my_data[y][x] = 0
                        y = y + 1
                        x = x
                        # my_data[y + 1][x] = 0
                cnt += 1

            if y == 99:
                if cnt < result:
                    result = cnt
                    min_start = start
                    # print('######', start, cnt)
                # result.append(start, cnt)
                # print(f'#{tc}', cnt)

                break
    print(f'#{tc}', min_start)