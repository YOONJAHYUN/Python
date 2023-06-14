import sys

input = sys.stdin.readline


n, k, p, x = map(int, input().split())

numbers = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

num = str(x).zfill(k)

data = []
for i in num:
    data.append(numbers[int(i)])

ans = 0
for i in range(1, n+1):
    cnt = 0
    temp = []
    candi = str(i).zfill(k)

    for j in candi:
        temp.append(numbers[int(j)])

    for ii in range(k):
        for jj in range(7):
            if temp[ii][jj] != data[ii][jj]:
                cnt += 1
        if cnt > p:
            break

    if cnt <= p and cnt > 0:
        ans += 1
print(ans)