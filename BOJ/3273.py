import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())
data.sort()
cnt = 0

left = 0
right = n-1
while left < right:
    value = data[left] + data[right]

    if value == x:
        left += 1
        cnt += 1
    elif value > x:
        right -= 1
    elif value <x:
        left += 1

print(cnt)
