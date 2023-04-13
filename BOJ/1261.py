import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):

    heap = []
    heappush(heap, start)

    while heap:

        block, y, x = heappop(heap)


        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] > block:

                    if maze[ny][nx] == 1:




'''
빈방 or 벽
빈 방 자유롭게 다니기 가능
벽은 부수지 않으면 이동 불가능

여러명이 모두 같은 방
상하좌우 이동 가능

벽은 평소에 이동 불가능, 알고스팟 무기 사용하면 가능
벽을 부수면 빈방과 동일해짐

1,1에 있는 운영진이 N,M가려면 최소 몇개를 부숴야 하냐?
0 빈방 1 벽
'''
# 세로 N 가로 M
M,N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(M)]

visited = [[1e9] * M for _ in range(N)]

dijkstra(0, 0, 0)
print(visited[-1][-1])