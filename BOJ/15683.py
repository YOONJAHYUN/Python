import sys
from copy import deepcopy
input = sys.stdin.readline


def CCTV(cctv, y, x, data):

    new_room = deepcopy(data)
    if cctv == 1:
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            mul = 1
            ny, nx = y + dy*mul, x + dx*mul

            while True:
                if 0 <= ny < n and 0 <= nx < m and new_room[ny][nx] == 0:
                    new_room[ny][nx] = '#'
                else:
                    break
            return new_room



def check(depth, f, cnt):
    global ans

    if depth == f:
        ans = max(cnt, ans)
        return


    for i in range(f):
        cctv, y, x, = cctvs[i]
        CCTV(cctv, y, x, room)






'''
0 빈칸
6 벽
1~5 cctv

사각 지대의 최소 크기 구하기
'''
n, m = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

'''
총 공간을 먼저 구한다. n*m 에다가 cctv 갯수와 벽을 뺌.
cctv 별로 체크할 수 있는 부분을 표기
1 : dx dy [1, -1, 0, 0], [0, 0, -1, 1]
2 : 
cctv 경우의 수만큼 함수 돌리기
max 를 표기하고 백트래킹 형식으로 표기
'''

total = n * m
cctvs = []
ans = 0
for i in range(n):
    for j in range(m):
        if room[i][j] != 0:
            # 벽인 경우
            if room[i][j] == 6:
                total -= 1
            # cctv 인경우
            else:
                cctvs.append((room[i][j],i,j))
                total -= 1

check(0, len(cctvs), 0)