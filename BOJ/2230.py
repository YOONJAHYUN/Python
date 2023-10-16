import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [int(input()) for _ in range(n)]

data.sort()

ans = 2000000001

for i in range(n):
    num = data[i]

    right = i + 1

    while right < n:


        if data[right] - num >= m:
            ans = min(ans, data[right] - num)
            break

        else:
            right += 1


print(ans)