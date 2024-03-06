import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

def game(ans, i):
    global answer

    if i == 10 or horses.count((-1, -1)) == 4:
        answer = max(answer, ans)
        return

    # 말 이동
    num = data[i]

    for j in range(4):
        y, x = horses[j]
        oy, ox = y, x

        # 이미 도착한 말
        if y == -1 and x == -1:
            continue

        nx = x + num

        # 직진
        if len(board[y]) - 1 > nx:
            x = nx

        # 파란색에 위치했을 때 / 끝자락인경우
        elif len(board[y]) - 1 == nx:
            if y == 3 or y == 4 or y == 5 or y == 6:
                x = nx

            else:
                # 이동
                y, x = JUMP[y], 0

        # 다음 칸으로 변경해야할 때
        else:
            if (y == 3 or y == 4 or y == 5 or y == 6) and (nx >= len(board[y]) - 1):
                # 도착
                y, x = -1, -1
            else:
                y, x = MOVE[y], nx - len(board[y])

        if (y, x) == (4, 4) or (y, x) == (5, 3) or (y, x) == (6, 4):
            if (4, 4) in horses or (5, 3) in horses or (6, 4) in horses:
                continue

        if (y, x) == (4, 5) or (y, x) == (5, 4) or (y, x) == (6, 5):
            if (4, 5) in horses or (5, 4) in horses or (6, 5) in horses:
                continue

        if (y, x) == (4, 6) or (y, x) == (5, 5) or (y, x) == (6, 6):
            if (4, 6) in horses or (5, 5) in horses or (6, 6) in horses:
                continue

        if (y, x) == (3, 4) or (y, x) == (4, 7) or (y, x) == (5, 6) or (y, x) == (6, 7):
            if (3, 4) in horses or (4, 7) in horses or (5, 6) in horses or (6, 7) in horses:
                continue

        if y != -1 and (y, x) in horses:
            continue

        horses[j] = (y, x)
        game(ans+board[y][x], i+1)
        horses[j] = (oy, ox)


data = list(map(int, input().split()))
answer = 0
MOVE = {0: 1, 1: 2, 2: 3}
JUMP = {0: 4, 1: 5, 2: 6}

board = [[0, 2, 4, 6, 8, 10], [12, 14, 16, 18, 20], [22, 24, 26, 28, 30], [32, 34, 36, 38, 40], [10, 13, 16, 19, 25, 30, 35, 40], [20, 22, 24, 25, 30, 35, 40], [30, 28, 27, 26, 25, 30, 35, 40], [0]]

horses = [(0, 0), (0, 0), (0, 0), (0, 0)]

game(0, 0)

print(answer)

