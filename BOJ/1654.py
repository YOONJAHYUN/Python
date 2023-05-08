import sys
input = sys.stdin.readline

k, n = map(int, input().split())

data = [int(input()) for _ in range(k)]

start = 1
end = max(data)

while start <= end:

    mid = (start+end) // 2

    total = 0
    for line in data:
        total += (line//mid)

    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)