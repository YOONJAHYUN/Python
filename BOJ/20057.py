import sys
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
    print(x, y, d, c, dir_max)
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
    valid = 0
    now_sand = data[y][x]
    # 만약 모래가 있다면
    if now_sand:
        # 격자에 표기된 방향대로 모래가 이동한다
        for i in range(9):
            dir, sand = tornado[i]
            dx, dy = dir

            nx, ny = dx*mul[d%4][0]+x, dy*mul[d%4][1]+y
            if 0 <= nx < n and 0 <= ny < n:
                data[ny][nx] += floor(now_sand * (sand / 100))
                valid += floor(now_sand * (sand / 100))

            now += floor(now_sand * (sand / 100))

        nx = -1*mul[d%4][0]+x
        if 0 <= nx < n:
            data[y][nx] += now_sand - now
        # 남은 모래 구하기
        answer += now_sand - valid
        data[y][x] = 0

    if y == 0 and x == 0:
        return

    # 모래 이동이 끝난 후, 새로 방향 조절
    Move(y, x, d, c)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

directions = {
    0: [-1, 0],
    1: [0, 1],
    2: [1, 0],
    3: [0, -1]
}
# (x, y), 퍼센트
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
    0: [1, 1],
    1: [1, -1],
    2: [-1, -1],
    3: [-1, 1]
}

# 스타트
y, x = n//2, n//2

dir_max = 0
answer = 0
# 토네이도 달팽이 형식으로
Tornado(y, x, 3, 1)
print(answer)

for i in data:
    print(i)