import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

ans = 0

start = 0
end = 20*n
while start <= end:

    # 그룹들의 최소가 mid인가?
    mid = (start + end) // 2

    my_sum = 0
    count = 0

    for i in range(n):
        my_sum += data[i]
        if my_sum >= mid:
            count += 1
            my_sum = 0

    if count >= k:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
