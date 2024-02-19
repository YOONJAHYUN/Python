import sys

input = sys.stdin.readline

def binary_search(start, end, target):

    while start <= end:
        mid = (start + end) // 2
        if result[mid] == target:
            return mid

        if result[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start



n = int(input())

lst = list(map(int, input().split()))
result = []

for i in range(n):
    num = lst[i]
    if not len(result) or result[-1] < num:
        result.append(num)
    else:
        temp = binary_search(0, len(result) - 1, num)
        result[temp] = num

print(len(result))
