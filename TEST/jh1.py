import sys

sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    # switch 0 x증가방향
    # switch 1 y증가방향
    # switch 2 x감소방향
    # switch 3 y감소방향

    # 현재 나의 위치
    x, y = 0, 0

    switch = 0
    # 직진과 오른쪽 회전만 가능.
    apple = 1
    cnt = 0
    apple_max = 0
    for i in range(N):
        for j in range(N):
            apple_max = max(apple_max, data[i][j])

    # 첫번째 사과의 위치를 찾자.
    while apple <= apple_max:
        for i in range(N):
            for j in range(N):

                if data[i][j] == apple:

                    ax, ay = j, i

                    if switch == 0:
                        if ax - x > 0 and ay - y > 0:   # 오-위
                            cnt += 1
                        elif ax - x < 0 and ay - y< 0:  # 왼-아래
                            cnt += 3
                        elif ax - x > 0 and ay - y < 0: # 왼-위
                            cnt += 3
                        elif ax - x < 0 and ay - y>0:   # 오-아래
                            cnt += 2
                        elif ax - x > 0 and ay - y == 0:    # 위
                            cnt += 0
                        elif ax - x < 0 and ay - y == 0:    # 아래
                            cnt += 3
                        elif ax - x == 0 and ay - y > 0:    # 좌
                            cnt += 3
                        elif ax - x == 0 and ay - y < 0:    # 우
                            cnt += 1
                        x, y = j, i
                        apple += 1
                        switch = cnt % 4

                    elif switch == 2:
                        if ax - x < 0 and ay - y < 0:  # 오-위
                            cnt += 1
                        elif ax - x > 0 and ay - y > 0:  # 왼-아래
                            cnt += 3
                        elif ax - x < 0 and ay - y > 0:  # 왼-위
                            cnt += 3
                        elif ax - x > 0 and ay - y < 0:  # 오-아래
                            cnt += 2
                        elif ax - x < 0 and ay - y == 0:  # 위
                            cnt += 0
                        elif ax - x > 0 and ay - y == 0:  # 아래
                            cnt += 3
                        elif ax - x == 0 and ay - y > 0:  # 좌
                            cnt += 3
                        elif ax - x == 0 and ay - y < 0:  # 우
                            cnt += 1
                        x, y = j, i
                        apple += 1
                        switch = cnt % 4

                    elif switch == 1:
                        if ax - x < 0 and ay - y > 0:  # 오-위
                            cnt += 1
                        elif ax - x > 0 and ay - y < 0:  # 왼-아래
                            cnt += 3
                        elif ax - x > 0 and ay - y > 0:  # 왼-위
                            cnt += 3
                        elif ax - x < 0 and ay - y < 0:  # 오-아래
                            cnt += 2
                        elif ax - x == 0 and ay - y > 0:  # 위
                            cnt += 0
                        elif ax - x == 0 and ay - y < 0:  # 아래
                            cnt += 3
                        elif ax - x > 0 and ay - y == 0:  # 좌
                            cnt += 3
                        elif ax - x < 0 and ay - y == 0:  # 우
                            cnt += 1
                        x, y = j, i
                        apple += 1
                        switch = cnt % 4

                    elif switch == 3:
                        if ax - x > 0 and ay - y < 0:  # 오-위
                            cnt += 1
                        elif ax - x < 0 and ay - y > 0:  # 왼-아래
                            cnt += 3
                        elif ax - x < 0 and ay - y < 0:  # 왼-위
                            cnt += 3
                        elif ax - x > 0 and ay - y > 0:  # 오-아래
                            cnt += 2
                        elif ax - x == 0 and ay - y < 0:  # 위
                            cnt += 0
                        elif ax - x == 0 and ay - y > 0:  # 아래
                            cnt += 3
                        elif ax - x < 0 and ay - y == 0:  # 좌
                            cnt += 3
                        elif ax - x > 0 and ay - y == 0:  # 우
                            cnt += 1
                        x, y = j, i
                        apple += 1
                        switch = cnt % 4


    print(f'#{tc}', cnt)