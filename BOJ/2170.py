import sys

input = sys.stdin.readline

n = int(input())

data = list(tuple(map(int, input().split())) for _ in range(n))

data.sort()

start, end = data[0]

ans = end - start

for next_start, next_end in data[1:]:

    if next_start < end:
        if next_end < end:
            continue
        ans += (next_end-end)

        end = next_end

    else:
        ans += (next_end - next_start)
        start, end = next_start, next_end

print(ans)