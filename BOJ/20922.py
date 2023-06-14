import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

lst = [0] * 100001

left = 0
right = 0

ans = 0

while right < n:

    left_val = data[left]
    right_val = data[right]

    if lst[right_val] + 1 <= k:
        lst[right_val] += 1
        right += 1
        ans = max(ans, right-left)
    else:
        lst[left_val] -= 1
        left += 1

print(ans)