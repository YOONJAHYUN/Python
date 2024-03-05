import sys

input = sys.stdin.readline

'''
1. 흰색인 경우 그 칸으로 이동. 이동하려는 칸에 말이 있으면 가장 위에 올림
2. 빨간색인 경우 이동한 후에 a번 말과 그 위에 잇는 모든 말의 쌓여있는 순서 변경.
3. 파란색인 경우 a번 말의 이동 방향을 반대로 하고 한 칸 이동.
- 방향을 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히
- 체스판을 벗어나는 경우도 파란색인 경우와 같음

게임이 종료되는 턴의 번호 : 턴이 진행되던 중에 말이 4개 이상 쌓이면 끝

0 흰색
1 빨간
2 파란
'''

def move(y, x, ny, nx, i):
    # 그 위에 쌓인 게 있는 지 체크
    idx = chessboard[y][x].index(i)
    tmp = []

    while idx < len(chessboard[y][x]):
        tmp.append(chessboard[y][x].pop())

    # 흰색인 경우
    if arr[ny][nx] == 0:
        tmp = tmp[::-1]
    # 자리 이동
    for now in tmp:
        chessboard[ny][nx].append(now)
        chess_piece[now] = [ny, nx, chess_piece[now][2]]

    if len(chessboard[ny][nx]) >= 4:
        print(answer)
        exit(0)

    if answer > 1000:
        print(-1)
        exit(0)

DIR = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
opp_dr = {1:2, 2:1, 3:4, 4:3}

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
chessboard = [[[] for _ in range(n)] for _ in range(n)]
chess_piece = []

for i in range(k):
    a, b, c = map(int, input().split())
    chessboard[a-1][b-1].append(i)
    chess_piece.append([a-1, b-1, c])

answer = 0

while True:
    answer += 1

    for i in range(k):
        y, x, d = chess_piece[i]
        # 이동할 곳 탐색
        ny, nx = y+DIR[d][0], x+DIR[d][1]

        # 체스판 내에 있고 파란색이 아닌 경우
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 2:
            move(y, x, ny, nx, i)

        # 체스판이 파란색이거나 체스판 외로 가는 경우
        else:
            # 방향전환
            d = opp_dr[d]

            chess_piece[i][2] = d

            ny, nx = y + DIR[d][0], x + DIR[d][1]

            # 그 방향이 다시 파란색이라면?
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 2:
                move(y, x, ny, nx, i)
