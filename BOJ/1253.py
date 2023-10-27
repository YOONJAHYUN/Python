import sys

input = sys.stdin.readline

def find(x):
    global count
    start = 0
    end = n - 1

    while (start < end):



        temp = data[start] + data[end]

        if (start != x and end != x) and temp == data[x]:
            return True


        if temp < data[x] or start == x:
            start += 1

        else:
            end -= 1
    return False


n = int(input())
data = list(map(int, input().split()))
data.sort()
# print(data)

count = 0
for i in range(n):
    if find(i):
        count += 1
        # print(i)

print(count)