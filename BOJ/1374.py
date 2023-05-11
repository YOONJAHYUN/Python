import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x:x[1])
q = []
heappush(q, (data[0][2]))

for i in range(1, n):
    c, s, e = data[i]

    if q[0] <= s:
        heappop(q)
    heappush(q, e)
print(len(q))
