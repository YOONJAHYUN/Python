import sys

input = sys.stdin.readline

C, R = map(int, input().split())

K = int(input())

mat = [[0]*C for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
k = 0
idx = 2
mat[0][0]= 1
i = 0
x = 0
y = 0
while idx != R*C+1:
    if x%R+ dx[k%4] >= R or y%C +dy[k%4] >= C or mat[x%R+dx[k%4]][y%C+dy[k%4]] !=0:
        k += 1
        mat[x%R+dx[k % 4]][y%C+ dy[k % 4]] = idx
        idx += 1

    else:
        mat[x%R+dx[k%4]][y%C+dy[k%4]] = idx
        idx += 1
    if k% 4 == 0:
        x += 1
    elif k % 4 == 1:
        y += 1
    elif k % 4 == 2:
        x -= 1
    elif k % 4 == 3:
        y -= 1
result = []
for i in range(R):
    for j in range(C):
        if mat[i][j] == K:
            result = (j+1, i+1)
            break
if result:
    print(*result)

else:
    print(0)