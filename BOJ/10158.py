import sys

input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) % (2 * w)
y = (q + t) % (2 * h)

if x > w:
    x = w - (x - w)
if y > h:
    y = h - (y-h)


print(x, y)