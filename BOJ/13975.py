import sys
from heapq import heappop, heappush
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    result = 0
    while data:
        num1 = heappop(data)
        num2 = heappop(data)

        x = num1 + num2
        result += x
        heappush(data, x)

        if len(data) == 1:
            print(result)
            break
