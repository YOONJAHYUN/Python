import sys
input = sys.stdin.readline

# 플로이드 와샬 알고리즘
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if data[j][i] and data[i][k]:
                data[j][k] = 1

for i in data:
    print(*i)