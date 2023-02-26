import sys

input = sys.stdin.readline

w, h = map(int, input().split())

# 종이를 자르지말고, 애초에 종이를 만들때 이 값들을 모두 모아서만들고 잘라버리자.
n = int(input())
line0 = []
line1 = []
dots0 = []
dots1 = []
for _ in range(n):
    line, dot = map(int, input().split())
    if line == 0:
        line0.append(line)
        dots0.append(dot)
    else:
        line1.append(line)
        dots1.append(dot)

paper = [[0]*(w+len(line1)) for _ in range(h+len(line0))]

dots0.sort()
dots1.sort()
idx1 = 0

for i in dots0:
    paper[i+idx1] = [1]*(w+len(line1))
    idx1 += 1

idx2 = 0

for i in dots1:
    for j in range(h + len(line0)):
        paper[j][i+idx2] = 1
    idx2 += 1

for i in paper:
    print(i)

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

visited = [[0]*(w+len(line1)) for _ in range(h + len(line0))]
stack = []
result = []

stack.append((0, 0))
visited[0][0] = 1

while stack:
    while stack:

        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < h + len(line0) and 0 <= nj < w + len(line1):
                if visited[ni][nj] == 0 and paper[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    stack.append((ni, nj))

    for ci in range(h + len(line0)):
        for cj in range(w + len(line1)):
            if visited[ci][cj] == 0 and paper[ci][cj] == 0:
                stack.append((ci, cj))
                visited[ci][cj] = 1

print('########################')
for i in visited:
    print(i)




