import sys
from collections import Counter
input = sys.stdin.readline

def check(move):
    global y, x, mad
    # 움직일 방향
    mmove = moving[move]
    # 종수가 움직였음
    ny, nx = y + mmove[0], x + mmove[1]
    # 종수 초기화
    data[y][x] = '.'

    # 이동했는데 미친아두이노 있으면 탈락
    if data[ny][nx] == 'R':
        return False
    # 종수 옮기기
    data[ny][nx] = 'I'
    y, x = ny, nx
    new = []
    # 미친 아두이노도 움직여야됨
    for my, mx in mad:
    # while mad:
    #     my, mx = mad.pop()
        dy = ny - my
        dx = nx - mx

        # 일단 초기화
        data[my][mx] = '.'
        # 아두이노가 새로 움직일 곳
        gy, gx = my, mx
        # 움직임 표시
        if dy == 0 and dx == 0:
            gy, gx = my, mx
        elif dy < 0 and dx == 0:
            gy, gx = my-1, mx
        elif dy > 0 and dx == 0:
            gy, gx = my+1, mx
        elif dy == 0 and dx > 0:
            gy, gx = my, mx+1
        elif dy == 0 and dx < 0:
            gy, gx = my, mx-1
        elif dy > 0 and dx > 0:
            gy, gx = my+1, mx+1
        elif dy < 0 and dx < 0:
            gy, gx = my-1, mx-1
        elif dy > 0 and dx < 0:
            gy, gx = my+1, mx-1
        elif dy < 0 and dx > 0:
            gy, gx = my-1, mx+1

        # 미친아두이노가 움직였다.
        # 근데 종수가 있으면 종수가짐
        if data[gy][gx] == 'I':
            return False
        # 아니라면 일단 저장
        new.append((gy, gx))

    count = Counter(new)
    real = []

    for ay, ax in new:
        if count[(ay, ax)] > 1:
            continue
        else:
            data[ay][ax] = 'R'
            real.append((ay, ax))

    mad = real
    return True


r, c = map(int, input().split())

# '.'는 빈 칸, 'R'은 미친 아두이노, 'I'는 종수의 위치
data = [list(input().rstrip()) for _ in range(r)]
# 종수가 움직이려고 하는 방향
dir = list(map(int, input().rstrip()))

# 움직이는 방향
moving = [[], [1, -1], [1, 0], [1, 1], [0, -1], [0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

# 종수의 위치
y, x = 0, 0

# 미친 아두이노의 위치
mad = []

for i in range(r):
    for j in range(c):
        if data[i][j] == 'I':
            y, x = i, j
        elif data[i][j] == 'R':
            mad.append((i, j))

for i in range(len(dir)):
    if not check(dir[i]):
        print("kraj", i+1)
        exit(0)

for i in range(r):
    print(''.join(data[i]))