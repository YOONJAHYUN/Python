import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    d, w = map(int, input().split())
    data.append((-d, -w))

data.sort()
# print(data)
ans = 0

now = data[0][0]

while True:
    q = []
    for i in range(len(data)):
        day, work = data[i]
        if day <= now:
            # print(day, work)
            heappush(q, (work, day))

        else:
            break
    if q:
        work, day = heappop(q)
        ans += work

        idx = data.index((day, work))
        data.pop(idx)

    now += 1
    if now == 0:
        break

print(-ans)





