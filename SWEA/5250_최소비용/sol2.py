import sys
from collections import deque
sys.stdin = open('input.txt')

# dp로 풀면 안됨 ;;
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 높이는 높이일뿐이니까 걍 최댓값 넣어주기
    visited = [[1e9]*N for _ in range(N)]

    q = deque()

    # 그냥 값넣어주는건 튜플로 넣기
    q.append((0, 0))
    visited[0][0] = 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] > 1 + max(data[ny][nx]-data[y][x], 0) + visited[y][x]:
                    visited[ny][nx] = 1 + max(data[ny][nx]-data[y][x], 0) + visited[y][x]
                    q.append((ny,nx))


    print(f'#{tc}', visited[-1][-1])





