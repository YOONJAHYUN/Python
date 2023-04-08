import sys
from collections import deque
input = sys.stdin.readline

# 문어박사님 임포트함....

def bfs(si, sj):
    q = deque()
    vv = [[0]*5 for _ in range(5)]

    q.append((si, sj))
    vv[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 조건에서 원래방문했던 애로 가야됨
            if 0 <= ni < 5 and 0 <= nj < 5 and vv[ni][nj] == 0 and v[ni][nj] == 1:
                q.append((ni, nj))
                vv[ni][nj] = 1
                cnt += 1
    # 다 방문했을 때 7이라면 True반환
    return cnt == 7


def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                # 방문한걸 찾아서 bfs
                return bfs(i, j)

'''
2차원 배열을 1차원 배열로 만든다.
학생을 일렬로 줄 세우고, SYSY 조합을 구한다.

'''
# 가능한 조합을 모두 구한거임
def dfs(n, cnt, scnt):
    global ans

    # 가지치기
    if cnt > 7:
        return

    # 종료조건
    if n == 25:
        # 7개가 선택되어야 하고, S파가 4명이상
        if cnt == 7 and scnt >= 4:
            # 조건을 채웠는데, 이게 인접해 있는지 확인
            # 체크했을 때 true면 ans += 1해주기
            if check():
                ans += 1
        return

    # 포함하는 경우
    v[n//5][n%5] = 1
    # S라면 true가 나오고 이는 int로 변환시 + 1
    dfs(n+1, cnt+1, scnt+int(data[n//5][n%5]=='S'))
    # 포함하지 않는 경우
    v[n//5][n%5] = 0
    dfs(n+1, cnt, scnt)

data = [list(input().rstrip()) for _ in range(5)]
ans = 0
v = [[0]*5 for _ in range(5)]

dfs(0,0,0)
print(ans)
