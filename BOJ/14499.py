import sys
input = sys.stdin.readline

N, M, y, x, k = map(int, input().split())
arr = []
# 주사위 전개도
dice = [0, 0, 0, 0, 0, 0]
dice_move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
for _ in range(N):
    arr.append(list(map(int, input().split())))
order = list(map(int, input().split()))

# 주사위이동
def turn(num):
    global dice
    a, b, c, d, e, f = dice

    if num == 1:
        dice = [d, b, a, f, e, c]
    elif num == 2:
        dice = [c, b, f, a, e, d]
    elif num == 3:
        dice = [e, a, c, d, f, b]
    else:
        dice = [b, f, c, d, a, e]

for i in range(k):
    move = order[i]
    dy, dx = dice_move[move]

    ny, nx = y + dy, x + dx

    if 0 <= ny < N and 0 <= nx < M:
        turn(move)
        if arr[ny][nx] == 0:
            arr[ny][nx] = dice[5]
        else:
            dice[5] = arr[ny][nx]
            arr[ny][nx] = 0
        print(dice[0])
        y, x = ny, nx


