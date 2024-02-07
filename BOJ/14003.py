import sys
input = sys.stdin.readline

def binary_search(left, right, target):

    while left <= right:

        mid = (left + right) // 2

        if result[mid] == target:
            return mid

        if result[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

n = int(input())
data = list(map(int, input().split()))
result = []
record = [0] * n

for i in range(n):
    num = data[i]
    if len(result) == 0 or result[-1] < num:
        result.append(num)
        record[i] = len(result) - 1
    else:
        temp = binary_search(0, len(result)-1, num)
        result[temp] = num
        record[i] = temp

print(len(result))

my_max = max(record)
answer = []
for i in range(n-1, -1, -1):
    if record[i] == my_max:
        answer.append(data[i])
        my_max -= 1

    if my_max == -1:
        print(*answer[::-1])
        break
