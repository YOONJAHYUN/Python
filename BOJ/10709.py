import sys

input = sys.stdin.readline

H, W = map(int, input().split())

cloud = [list(input().rstrip()) for _ in range(H)]

when_cloud = [[-1]*W for _ in range(H)]

for i in range(H):
    if 'c' not in cloud[i]:
        continue
    else:
        for j in range(W):
            if cloud[i][j] == 'c':
                when_cloud[i][j] = 0
                cnt = 0
            else:
                idx = cloud[i].index('c')
                if j < idx:
                    when_cloud[i][j] = -1
                else:
                    cnt += 1
                    when_cloud[i][j] = cnt

for i in when_cloud:
    print(*i)