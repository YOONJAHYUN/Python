import sys
# from heapq import heappop, heappush
input = sys.stdin.readline

N, D = map(int, input().split())

way = [i for i in range(D+1)]
data = []
for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D and d < (e-s):
        data.append((s, e, d))

# data.sort()
for i in range(D+1):
    way[i] = min(way[i-1]+1, way[i])

    for s, e, d in data:
        if way[s] + d < way[e]:
            way[e] = way[s] + d
print(way[-1])

