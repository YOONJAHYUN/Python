import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())

heap = []
data = list(map(int, input().split()))

for i in data:
    heappush(heap, i)

for _ in range(m):
    num1 = heappop(heap)
    num2 = heappop(heap)

    heappush(heap, num1+num2)
    heappush(heap, num1+num2)

print(sum(heap))