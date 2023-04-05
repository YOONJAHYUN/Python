import sys
input = sys.stdin.readline

def cleaning(y, x, d):
    global result
    # for i in room:
    #     print(i)
    # print()
    # print(y,x,d)
    # print(result)

    # 현재 칸 청소안되면 청소하기
    if room[y][x] == 0:
        room[y][x] = 2
        result += 1

    # 상하좌우 조사
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        # 조사했을 때

        if 0 <= ny < N and 0 <= nx < M:
            if room[ny][nx] == 0:
                cnt += 1
                break
    # 청소되지 않은 빈 칸이 없는 경우
    if cnt == 0:
        # 후진할수 있는 지 확인
        # 북쪽을 보는 경우
        if d == 0:
            y += 1

        # 동쪽
        elif d == 1:
            x -= 1

        # 남쪽
        elif d == 2:
            y -= 1

        # 서쪽
        else:
            x += 1

        # 뒤로 갈 수 있냐?
        # 벽이아니다
        if room[y][x] != 1:
            # 다시 청소시작
            cleaning(y, x, d)
        # 벽이다.
        else:

            return

    # 청소할 수 있다면?
    else:
        d = (d-1)%4

        while True:
            ry = y
            rx = x
        # 반시계방향으로 회전
        # 바라보는 방향에서 앞쪽 칸이 청소되었나?
        # 북쪽을 보는 경우
            if d == 0:
                ry -= 1
                # y -= 1

            # 동쪽
            elif d == 1:
                # dx = x + 1
                rx += 1
            # 남쪽
            elif d == 2:
                # dy = y + 1
                ry += 1
            # 서쪽
            else:
                # dx = x - 1
                rx -=1


            if room[ry][rx] == 0:
                cleaning(ry, rx, d)
                return


            else:
                d = (d - 1) % 4



N, M = map(int, input().split())
# 로봇 청소기 위치, 방향
r, c, d = map(int,input().split())

'''
d
0 북쪽
1 동쪽
2 남쪽
3 서쪽
'''

'''
현재 칸 청소

주변 4칸 중 청소가 다 되어잇다면
방향 유지한채로 후진하고 다시 
후진 불가능? 작동멈추기

주변 4칸 중 청소되지 않은 빈칸이 있다면
반시계 방향으로 90도 회전
앞칸이 청소 안됨? -> 한 칸 전진
다시
'''

# 0 청소안됨 1 벽 2 청소완료
room = [list(map(int,input().split())) for _ in range(N)]
result = 0
cleaning(r, c, d)
print(result)
