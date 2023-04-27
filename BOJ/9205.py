import sys
from collections import deque
input = sys.stdin.readline



def check(start):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        if abs(y-ey) + abs(x-ex) <= 1000:
            print('happy')
            return

        for i in range(n):
            nx, ny = stores[i]
            if abs(y-ny) + abs(x-nx) <= 1000 and not visited[i]:
                visited[i] = True
                q.append((nx, ny))

    print('sad')
    return

t = int(input())

for _ in range(t):
    n = int(input())
    flag = False
    # 집
    start = tuple(map(int, input().split()))
    stores = []

    # 편의점
    for _ in range(n):
        x, y = map(int, input().split())
        stores.append((x, y))
    visited = [False for _ in range(n)]

    # 페스티벌
    ex, ey = map(int, input().split())

    check(start)
