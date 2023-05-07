import sys
input = sys.stdin.readline

n, c = map(int, input().split())

data = [int(input()) for _ in range(n)]
data.sort()
start = 1
end = data[-1] - data[0]

while start <= end:

    mid = (start+end) // 2

    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] >= current + mid:
            count += 1
            current = data[i]

    if count >= c:
        start = mid + 1
    else:
        end = mid - 1
print(end)
