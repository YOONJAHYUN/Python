import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())

        data = [int(input()) for _ in range(n)]
        data.sort()

        left = 0
        right = n-1

        while left < right:

            if data[left] + data[right] == x:
                print("yes", data[left], data[right])
                break


            if data[left] + data[right] < x:
                left += 1
            else:
                right -= 1

        else:
            print("danger")
    except:
        break

