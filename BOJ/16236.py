import sys
# from collections import deque
from heapq import heappop,heappush
input = sys.stdin.readline

n = int(input())

def find_fish(i, j):
    global eat, size, ni, nj, count

    q = []
    heappush(q, (0, i, j))

    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True

    while q:
        cnt, y, x = heappop(q)
        # y, x, cnt = q.popleft()

        if arr[y][x] and arr[y][x] < size:
            # print("here",y, x, arr[y][x])
            # print("size", size)
            eat += 1
            arr[y][x] = 0
            count += cnt

            if eat == size:
                size += 1
                eat = 0
                # print("size", size)

            find_fish(y, x)

        for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):

            ny, nx = y+dy, x+dx

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if arr[ny][nx] <= size:
                    heappush(q, (cnt+1, ny, nx))
                    # q.append((ny, nx, cnt+1))
                    visited[ny][nx] = True

    return


ni, nj = 0, 0
size = 2
eat = 0

arr = []

count = 0

for i in range(n):
    temp = list(map(int, input().split()))
    if 9 in temp:
        ni = i
        nj = temp.index(9)
    arr.append(temp)

arr[ni][nj] = 0
find_fish(ni, nj)

print(count)


