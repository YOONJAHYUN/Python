import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s,t))

data.sort(key=lambda x:(x[1]-x[0], x[0]))
visited = [False] * n
# print(data)

cnt = 0
count = 0
while True:
    cnt += 1
    start, end = 0, 0
    for i in range(n):
        if not visited[i]:
            start, end = data[i]
            visited[i] = True
            count += 1
            break
    for i in range(1, n):
        s, e = data[i]
        if s >= end:
            end = e
            visited[i] = True
            count += 1
    if count == n:
        break
print(cnt)




