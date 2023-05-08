import sys
from heapq import heappop, heappush
input = sys.stdin.readline


n = int(input())
data = []
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s,t))

data.sort()
q = []
# 종료시간을 넣는다.
heappush(q, data[0][1])

for i in range(1,n):
    if data[i][0] >= q[0]:
        heappop(q)
    heappush(q, data[i][1])

print(len(q))

