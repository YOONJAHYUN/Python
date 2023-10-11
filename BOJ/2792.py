import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [int(input()) for _ in range(m)]

start, end = 1, max(data)


while start <= end:
    # mid 나눠가질 색
    mid = (start+end) // 2

    total = 0
    for d in data:
        # total 에 사람 수가 들어감
        if d % mid:
            total += (d//mid) + 1
        else:
            total += (d//mid)
    # 사람이 n명보다 많다면 더 많이 나눠가져갈 수 있음
    if total > n:
        start = mid + 1
    else:
        end = mid - 1

print(start)