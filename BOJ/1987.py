import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def DFS(y, x, words):
    global my_max
    my_max = max(my_max, words)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and not data[ny][nx] in sett:
            sett.add(data[ny][nx])
            DFS(ny, nx, words+1)
            sett.remove((data[ny][nx]))

R, C = map(int, input().split())
data = [list(input().rstrip()) for _ in range(R)]
my_max = 0
sett = set()
sett.add(data[0][0])
DFS(0, 0, 1)
print(my_max)