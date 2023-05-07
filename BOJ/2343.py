import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))

start = max(data)
end = sum(data)

ans = end
vm = start
while start <= end:

    mid = (start + end) // 2

    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if current + data[i] > mid:
            current = data[i]
            count += 1
        else:
            current += data[i]

    # 더 많이 만들어졌으면, 크기를 키워준다.
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        if mid >= vm:
            ans = min(ans, mid)
print(ans)
