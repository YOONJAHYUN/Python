import sys
input = sys.stdin.readline
from collections import deque

'''
나보다 큰거밖에 없으면 엄마상어에게 도움
1마리면 그 물고기
더많으면 가장 가까운거
거리가 같다면 가장 위, 가장 왼쪽 순으로

크기와 같은 수의 물고기를 먹을때마다 1 증가

아기상어 크기는 2

'''
def bfs(y, x):
    global eat, baby_power

    q = deque

    for shark in sharks:
        power, i, j = shark

        if power < baby_power:
            q.append((i, j))



n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

baby = []
baby_power = 2
eat = 0

sharks = []
# 아기 상어 위치 찾기
# 다른 상어 위치 표기
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            baby = (i, j)
        elif data[i][j]:
            sharks.append((data[i][j], i, j))
sharks.sort()
print(sharks)

bfs(baby[0], baby[1])


