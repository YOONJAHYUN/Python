import sys
input = sys.stdin.readline

def change():
    global dice
    # 동쪽
    if direction == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 서쪽
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 남쪽
    elif direction == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    # 북쪽
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]


n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# 동, 남, 서, 북
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

direction = 0 # 처음엔 동쪽으로 움직인다.

# 주사위 : 위,뒤,우,좌,앞,아래
dice = [1,2,3,4,5,6]

ny, nx = 0, 0

ans = 0

for _ in range(k):

    # arr 벗어나는 경우는 이동방향 반대로
    if ny+DIR[direction][0] >= n or ny + DIR[direction][0] < 0 or 0 > nx+DIR[direction][1] or nx+DIR[direction][1] >= m:
        direction += 2
        direction %= 4

    # 주사위 도면 바꾸기
    change()

    # 주사위 도착한 칸 점수
    q = []
    ny, nx = ny+DIR[direction][0], nx+DIR[direction][1]

    q.append((ny, nx))
    score = arr[ny][nx]
    cnt = 0

    visited = [[False] * m for _ in range(n)]
    visited[ny][nx] = True
    while q:
        y, x = q.pop()
        cnt += 1

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            sy, sx = y+dy, x+dx

            if 0 <= sy < n and 0 <= sx < m and not visited[sy][sx] and arr[sy][sx] == score:
                visited[sy][sx] = True
                q.append((sy, sx))

    # 이동방향 변경
    if dice[5] > score:
        # 시계방향
        direction += 1
    elif dice[5] < score:
        # 반시계방향
        direction -= 1

    direction %= 4

    ans += cnt * score

print(ans)














