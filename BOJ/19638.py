import sys
from heapq import heappop, heappush
input = sys.stdin.readline


n, h, t = map(int, input().split())

q = []

for _ in range(n):
    heappush(q, -(int(input())))

count = 0

for _ in range(t):
    if q[0] == -1 or - q[0] < h:
        break
    now = - heappop(q)

    heappush(q, -(now // 2))

    count += 1

if - q[0] < h:
    print("YES")
    print(count)
else:
    print("NO")
    print(-q[0])



