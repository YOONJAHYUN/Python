import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = list(map(int, input().split()))

while True:

    next = 0
    for i in range(n):
        num = data[i]

        if data[i+1]:
