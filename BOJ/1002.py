import sys
input = sys.stdin.readline




T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    r3 = sqrt(abs(x1-x2) ** 2 + abs(y1-y2) ** 2)


