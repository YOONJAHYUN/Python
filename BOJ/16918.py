import sys
input = sys.stdin.readline
dy = [1,-1,0,0]
dx = [0,0,-1,1]
def bomb(depth, n):
    if depth == n:
        for i in data:
            print(''.join(i))
        return

    bom = []
    for i in range(R):
        for j in range(C):
            if data[i][j] == 'O':
                bom.append([i,j])

    for y, x in bom:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < R and 0 <= nx < C and data[ny][nx] == '.':
                data[ny][nx] = 'O'

    for i in range(R):
        for j in range(C):
            if data[i][j] == '.':
                data[i][j] = 'O'
            else:
                data[i][j] = '.'

    bomb(depth+1, n)


R, C, N = map(int, input().split())

# 빈칸 . 폭탄O
data = [list(input().rstrip()) for _ in range(R)]
# 폭탄 폭발하면 인접한 칸도 파괴
# 인접칸에 폭탄이 있는 경우 -> 파괴 (연쇄반응없음)
bombbomb = [['O']*C for _ in range(R)]
# print(data)
if N % 2:
    bomb(0, N // 2)
else:

    for i in bombbomb:
        print(''.join(i))