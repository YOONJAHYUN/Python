import sys
from heapq import heappop,heappush
input = sys.stdin.readline

n = int(input())

q = []
my_max = 0
for _ in range(n):
    time, deadline = map(int, input().split())
    my_max = max(deadline, my_max)
    heappush(q, (-deadline, -time))


while q:
    if my_max < 0:
        break
    now_deadline, now_time = heappop(q)

    while my_max > - now_deadline:
        my_max -= 1

    my_max += now_time

print(-1) if my_max < 0 else print(my_max)




