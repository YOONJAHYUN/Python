import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))

start = 1
end = max(data)

while start <= end:
    mid = (start+end)//2

    total = 0
    for tree in data:
        if tree >= mid:
            total += (tree-mid)

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

