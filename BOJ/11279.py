import sys
input = sys.stdin.readline



N = int(input())

data = []

for _ in range(N):
    x = int(input())

    if x >= 1:
        data.append(x)

    elif x == 0:
        if not data:
            print(0)
        else:
            data.sort()
            print(data.pop())
