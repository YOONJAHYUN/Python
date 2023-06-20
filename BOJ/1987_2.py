import sys
input = sys.stdin.readline

def BFS(y, x, word):
    global ans

    ans = max(ans, len(word))

    for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny = y + dy
        nx = x + dx

        if 0 <= ny < R and 0 <= nx < C and data[ny][nx] not in word:
            BFS(ny, nx, word+data[ny][nx])


R, C = map(int, input().split())
ans = 0
data = [input().rstrip() for _ in range(R)]

# print(data)
#
BFS(0, 0, data[0][0])
print(ans)
