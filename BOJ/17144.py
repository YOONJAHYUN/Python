import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


'''
1
미세먼지는 4방향으로 확산
그 방향에 공기청정기가 있거나 or 칸이 없으면 그 방향으로 확산은 일어나지 않음
확산 양 : 나누기 /5 int처리
남은 양 : 원래있던거에 확산양뺀거

2
공기청정기 작동
위쪽은 반시계방향으로 순환
아래쪽은 시게방향으로 순환
미세먼지가 바람의 방향대로 한칸씩 이동

공기청정기에서 부는 바람은 미세먼지 없음. 
미세먼지 정화

공기청정기는 -1로 표기

방에 남아있는 미세먼지 양 구하기
'''

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def dust_check(depth, n):
    global data
    room = [[0]*C for _ in range(R)]

    if depth == n:

        result = 0
        for i in data:
            result += sum(i)
        print(result+2)
        return

    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            # 방에 미세먼지가 있다면
            if data[i][j]:
                dust = data[i][j]
                new_dust = int(dust/5)

                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    # 인접방향 체크
                    # 칸이 없거나 공기청정기가 있거나 의 대우
                    if 0 <= ny < R and 0 <= nx < C and data[ny][nx] != -1:
                        cnt += 1
                        room[ny][nx] += new_dust
                room[i][j] += dust - new_dust*cnt

    # 공기청정기 작동
    # 공기청정기 위치 잡기

    clean_y1 = 0
    clean_y2 = 0

    for i in range(R):
        if data[i][0] == -1:
            clean_y1 = i
            clean_y2 = i+1
            break
    # 공기청정기 room에 설치
    room[clean_y1][0] = -1
    room[clean_y2][0] = -1

    # ###
    # for i in room:
    #     print(*i)

    # 공기정청기 확산

    # cleaning1_x1 = room[clean_y1][1:C-1]
    # cleaning1_edge1 = room[clean_y1][C]
    # cleaning1_y1 = room[]
    #
    # print(cleaning1_x1)
    # room[clean_y1]

    x1 = 0
    y1 = clean_y1 - 1

    while y1 > 0:
        room[y1][x1] = room[y1-1][x1]
        y1 -= 1
    while x1 < C-1:
        room[y1][x1] = room[y1][x1+1]
        x1 += 1
    while y1 < clean_y1:
        room[y1][x1] = room[y1+1][x1]
        y1 += 1
    while x1 > 1:
        room[y1][x1] = room[y1][x1-1]
        x1 -= 1
    room[y1][x1] = 0
    # print()
    # for i in room:
    #     print(*i)

    x2 = 0
    y2 = clean_y2 + 1

    while y2 < R-1:
        room[y2][x2] = room[y2 + 1][x2]
        y2 += 1
    while x2 < C-1:
        room[y2][x2] = room[y2][x2 + 1]
        x2 += 1
    while y2 > clean_y2:
        room[y2][x2] = room[y2 - 1][x2]
        y2 -= 1
    while x2 > 1:
        room[y2][x2] = room[y2][x2 - 1]
        x2 -= 1
    room[y2][x2] = 0
    # print()
    #
    # for i in room:
    #     print(*i)
    data = room

    dust_check(depth+1, T)


R, C, T = map(int, input().split())

data = [list(map(int,input().split())) for _ in range(R)]

dust_check(0, T)