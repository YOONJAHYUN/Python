import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

sum_data = [0]
for i in data:
    sum_data.append(sum_data[-1]+i)

answer = int(1e9)


left = 0
right = 0

while left <= n and right <= n:

    if sum_data[right] - sum_data[left] >= s:
        answer = min(answer, right-left)
        left += 1
    else:
        right += 1

if answer == int(1e9):
    print(0)
else:
    print(answer)
