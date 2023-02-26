import sys

input = sys.stdin.readline

w, h = map(int, input().split())

n = int(input())
# line0 = []
# line1 = []
dots0 = []
dots1 = []
for _ in range(n):
    line, dot = map(int, input().split())
    if line == 0:
        # line0.append(line)
        dots0.append(dot)
    else:
        # line1.append(line)
        dots1.append(dot)

# print(dots0, dots1)
dots0.append(0)
dots0.append(h)
dots1.append(0)
dots1.append(w)
dots0.sort()
dots1.sort()

new_dots0 = []
new_dots1 = []

for i in range(1, len(dots0)):
    new_dots0.append(dots0[i] - dots0[i-1])

for i in range(1, len(dots1)):
    new_dots1.append(dots1[i] - dots1[i-1])

result = 0
for i in new_dots0:
    for j in new_dots1:
        if result < i*j:
            result = i*j
print(result)