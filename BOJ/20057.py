import sys
sys.setrecursionlimit(10**6)
from math import floor
input = sys.stdin.readline

'''
소수점 아래는 버림
토네이도는 (1, 1)까지 이동한 뒤 소멸한다.
모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때,
격자의 밖으로 나간 모래의 양을 구해보자.

토네이도 이동을 어떻게 하지?
-> 다음껄 구하는게 맞을듯
'''
def Move(y, x, d, c):
    global dir_max

    if (d == 0 or d == 2) and c == 1:
        dir_max += 1

    # 방향전환 필요없음
    if c < dir_max:
        dx, dy = directions[d%4]
        nx, ny = x+dx, y+dy
        Tornado(ny, nx, d%4, c+1)
    # 방향전환 필요함
    else:
        dx, dy = directions[(d+1)%4]
        nx, ny = x + dx, y + dy
        Tornado(ny, nx, (d+1)%4, 1)


def Tornado(y, x, d, c):
    global answer
    now = 0
    now_sand = data[y][x]
    # 만약 모래가 있다면
    if now_sand:
        # 격자에 표기된 방향대로 모래가 이동한다
        for i in range(9):
            dir, sand = tornado[i]
            dx, dy = dir

            if d == 0:
                nx, ny = dx+x, dy+y
            elif d == 2:
                nx, ny = -1*dx+x, dy+y
            elif d == 1:
                nx, ny = dy+x, -1 *dx+y
            else:
                nx, ny = dy+x, dx+y

            value = floor(now_sand * (sand / 100))

            now += value
            if 0 <= nx < n and 0 <= ny < n:
                data[ny][nx] += value
            else:
                answer += value

        if not d%2:
            xx = -1*mul[d%4][0]+x
            if 0 <= xx < n:
                data[y][xx] += now_sand - now
            else:
                answer += now_sand - now
        else:
            yy = -1 * mul[d % 4][1] + y
            if 0 <= yy < n:
                data[yy][x] += now_sand - now
            else:
                answer += now_sand - now

        # 남은 모래 구하기
        data[y][x] = 0

    if y == 0 and x == 0:
        return

    # 모래 이동이 끝난 후, 새로 방향 조절
    Move(y, x, d, c)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}
# (x, y), 퍼센트
# 좌 기준
'''
우 -> x만 -붙이기
상 -> y와 x 바꾸기
하 -> y와 x 바꾸고 -
'''
tornado = {
    0: [(1, -1), 1],
    1: [(0, -1), 7],
    2: [(-1, -1), 10],
    3: [(0, -2), 2],
    4: [(-2, 0), 5],
    5: [(1, 1), 1],
    6: [(0, 1), 7],
    7: [(-1, 1), 10],
    8: [(0, 2), 2],
    # 알파
    9: [(-1, 0), 0]
}

mul = {
    0: (1, 1),
    1: (-1, -1),
    2: (-1, -1),
    3: (1, 1)
}

# 스타트
y, x = n//2, n//2

dir_max = 0
answer = 0
# 토네이도 달팽이 형식으로
Tornado(y, x, 3, 1)

print(answer)
