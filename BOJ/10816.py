import sys

input = sys.stdin.readline

n = int(input())
data1 = list(map(int, input().split()))

m = int(input())
data2 = list(map(int, input().split()))

data1.sort()


dict = {}

for num in data1:
    if dict.get(num):
        dict[num] += 1
    else:
        dict[num] = 1

for num in data2:

    left = 0
    right = n - 1

    while left <= right:

        mid = (left+right) // 2

        if data1[mid] == num:
            print(dict[num], end=" ")
            break

        elif data1[mid] > num:
            right = mid - 1

        else:
            left = mid + 1
    else:
        print(0, end=" ")


