import sys
input = sys.stdin.readline

def check(s, e, beer):
    sx, sy = s
    ex, ey = e

    if abs(sx-ex) + abs(sy-ey) <= 1000:
        return "happy"

    for i in range(n):
        nx, ny = stores[i]

        check(s,e,)


t = int(input())

for _ in range(t):
    n = int(input())

    start = tuple(map(int, input().split()))
    stores = []

    # 편의점
    for _ in range(n):
        x, y = map(int, input().split())
        stores.append((x, y))


    # 집, 페스티벌
    end = tuple(map(int, input().split()))

    sx, sy = start
    ex, ey = end

    d = abs(sx-ex) + abs(sy-ey)
    print(d//50)

    check(start, end, 1000)