import sys
input = sys.stdin.readline

n, m = map(int, input().split())

times = [int(input()) for _ in range(n)]


start = 1
end = max(times) * m

ans = end
while start <= end:

    mid = (start + end) // 2


    total = 0
    for time in times:
        total += (mid//time)

    if total < m:
        start = mid + 1
    else:
        end = mid - 1
        ans = min(ans, mid)

print(ans)