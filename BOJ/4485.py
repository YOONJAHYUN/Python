import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def dijkstra(start):
    v[start[1]][start[2]] = start[0]

    heap = []
    heappush(heap, start)
    while heap:
        cost, y, x = heappop(heap)

        if v[y][x] < cost:
            continue

        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < N:
                res = data[ny][nx] + cost
                if res < v[ny][nx]:
                    v[ny][nx] = res

                    heappush(heap,(res, ny, nx))

number = 1
while True:

    N = int(input())

    if N == 0:
        break
    data = [list(map(int,input().split())) for _ in range(N)]
    v = [[1e9]*N for _ in range(N)]

    dijkstra((data[0][0],0, 0))

    print(f"Problem {number}:", v[N-1][N-1])
    number += 1

'''
상하좌우 한칸씩.
잃을 수 밖에 없는 최소 금액    
'''