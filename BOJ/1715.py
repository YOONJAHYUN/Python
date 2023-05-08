import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
# data = [int(input()) for _ in range(n)]
q = []

for _ in range(n):
    card = int(input())
    heappush(q,card)

cnt = 0
while True:
    if len(q) >= 2:
        num1 = heappop(q)
        num2 = heappop(q)
        heappush(q, num1+num2)
        cnt += num1 + num2
    else:
        print(cnt)
        break