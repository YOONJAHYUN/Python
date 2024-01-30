import sys

input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0
while True:

    if bin(n).count('1') <= k:
        break

    ans += 1
    n += 1

print(ans)
