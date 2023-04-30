import sys
input = sys.stdin.readline
sys.setrecursionlimit((10**6))
def DFS(y, x):

    # 아직 방문하지 않았을 때만 처리
    if not dp[y][x]:
        dp[y][x] = 1

        for dy, dx in ((0,1), (1, 0), (-1, 0), (0, -1)):
            ny, nx = dy+y, dx+x
            # 주위가 나보다 클 경우에만 경로 표시 가능 (작은 곳에서 큰 곳으로 가는 것)
            # 이친구 입장에서 갈 수 있는 곳을 표시 하는 중
            if 0 <= ny < n and 0 <= nx < n and data[ny][nx] > data[y][x]:
                # 좌표는 현재좌표와 주위를 다 돌았을 때
                dp[y][x] = max(DFS(ny, nx)+1, dp[y][x])

    return dp[y][x]


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, DFS(i,j))

print(answer)