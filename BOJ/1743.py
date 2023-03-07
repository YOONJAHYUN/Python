import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

# print(arr)
visited = [[False] * M for _ in range(N)]
# print(visited)
stack = []
# while stack:
my_max = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            stack.append((i, j))
            visited[i][j] = True
            cnt = 1

            while stack:
                ni, nj = stack.pop()


                di = [0, 0, -1, 1]
                dj = [-1, 1, 0, 0]

                for k in range(4):
                    si = ni + di[k]
                    sj = nj + dj[k]
                    if 0 <= si < N and 0 <= sj < M and arr[si][sj] and not visited[si][sj]:
                        visited[si][sj] = True
                        stack.append((si, sj))
                        cnt += 1
                if cnt > my_max:
                    my_max = cnt

print(my_max)

