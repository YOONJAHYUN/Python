import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def virus(depth, arr):
    global result
    if depth == 3:

        new_arr = deepcopy(arr)
        # 만들어진배열 확인
        # print("@@@@"*100)
        # for i in new_arr:
        #     print(i)
        # print("@@@@" * 100)
        # deque 설계
        q = deque()
        visited = [[False]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if new_arr[i][j] == 2:

                    q.append([i,j])

        dy = [1,-1,0,0]
        dx = [0,0,-1,1]

        while q:
            y, x = q.popleft()

            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and new_arr[ny][nx]== 0:
                    visited[ny][nx] = True
                    new_arr[ny][nx] = 2
                    q.append([ny,nx])
        # q가 끝나고나서
        cnt = 0
        for i in new_arr:
            cnt += i.count(0)
        # 바이러스   삐빕
        # print("VVVVVVVVVVVVVVVVV")
        # for i in new_arr:
        #     print(i)

        # print(cnt)
        result = max(cnt, result)
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1

                virus(depth+1, arr)
                arr[i][j] = 0


# 세로크기 N 가로크기 M
N, M = map(int, input().split())
# 0 빈칸 1 벽 2 바이러스
# 벽은 꼭 3개
data = [list(map(int, input().split())) for _ in range(N)]
result = 0
virus(0, data)
print(result)