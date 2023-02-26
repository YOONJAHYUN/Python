import sys

input = sys.stdin.readline

N = int(input())
paper = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):

    x, y, w, h = map(int, input().split())

    for j in range(y, y+h):
        for k in range(x, x+w):
            paper[j][k] = i

result = 0
num = 1
while num < N+1:
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == num:
                result += 1

    print(result)
    num += 1
    result = 0


