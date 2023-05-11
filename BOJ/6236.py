import sys
input = sys.stdin.readline


n, m = map(int, input().split())

data = [int(input()) for _ in range(n)]

# 무조건 용돈의 최대값보단 커야함
start = max(data)
end = sum(data)

ans = end

# 무조건 용돈의 최대값보단 커야함
# 그 기준점
vm = start

while start <= end:

    # 인출금액 k = mid인지
    mid = (start+end) // 2

    current = 0
    count = 1
    for i in range(n):
        if current + data[i] > mid:
            count += 1
            current = data[i]
        else:
            current += data[i]

    if count > m:
        start = mid + 1

    else:
        end = mid - 1
        if mid >= vm:
            ans = min(mid, ans)

print(ans)
