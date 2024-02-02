import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = []

def binary_search(left, right, target):

    while left <= right:

        mid = (left + right) // 2

        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

for num in a:
    if len(lis) == 0 or lis[-1] < num:
        lis.append(num)
    else:
        temp = binary_search(0, len(lis)-1, num)
        lis[temp] = num

print(len(lis))

