import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()
# 이전 구간과 새롭게 생긴 구간이 연속되는가?
target = 1
for num in data:
    if target < num:
        break

    target += num

print(target)

