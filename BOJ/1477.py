import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
print(data)


start = 1
end = l-1

while start <= end:

    mid = (start + end) // 2

    current = 1
    count = 0

    for i in range(len(data)):
        if data[i] >= mid + current:
            count += 1
            current = data[i]
            # ans = min(abs(data[i]-data[i-1]), ans)

    if count <= m:
        end = mid - 1
    else:
        start = mid + 1

print(end)



