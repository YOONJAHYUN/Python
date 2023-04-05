import sys
input = sys.stdin.readline

def DFS(y, x):
    global idx
    stack = [(y,x)]
    visited[y][x] = idx
    cnt = 1
    while stack:
        sj, si = stack.pop()
        # di = [1, -1, 0, 0]
        for dj, di in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nj = sj + dj
            ni = si + di

            if 0 <= ni < N and 0 <= nj < N:
                if arr[nj][ni] == 1 and visited[nj][ni] == 0:
                    visited[nj][ni] = idx
                    cnt += 1
                    stack.append((nj, ni))
    idx += 1
    return cnt

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

# print(arr)

visited = [[0]*N for _ in range(N)]
idx = 1
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:

            result.append(DFS(i,j))

result.sort()
n = len(result)
print(n)
for i in range(n):
    print(result[i])
