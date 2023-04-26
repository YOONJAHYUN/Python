import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())

link = []
for _ in range(n):
    a, b = map(int, input().split())
    link.append((a, b))
link.sort()


# 증가하는 방향
dp = [1]
x = [link[0][1]]
for i in range(1,n):
    a, b = link[i]

    if b > x[-1]:
        x.append(b)
        dp.append(dp[-1]+1)
    else:
        idx = bisect_left(x, b)
        x[idx] = b

ans = n-dp[-1]
print(ans)
