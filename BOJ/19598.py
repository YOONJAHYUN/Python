import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    s, e = map(int, input().split())
    data.append((s,e))

data.sort()

q = []

heappush(q, data[0][1])
for i in range(1, n):
    if data[i][0] >= q[0]:
        heappop(q)
    heappush(q, data[i][1])
print(len(q))