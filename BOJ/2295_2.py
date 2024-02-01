import sys

input = sys.stdin.readline

n = int(input())
data = sorted([int(input()) for _ in range(n)])

arr = []

for i in range(n):
    for j in range(i, n):
        arr.append(data[i]+data[j])

arr.sort()
answer = 0

for i in range(n):
    for j in range(i, n):
        temp = data[j] - data[i]

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left+right) // 2

            if arr[mid] == temp:
                answer = max(answer, data[j])
                break
            elif arr[mid] < temp:
                left = mid + 1
            else:
                right = mid - 1

print(answer)