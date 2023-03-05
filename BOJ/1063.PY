import sys

input = sys.stdin.readline

king, rock, N = input().split()

# print(king, rock, N)
N = int(N)
arr = [[0]*8 for _ in range(8)]
location = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
location_t = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
moving = {'R':(0, 1), 'L':(0, -1), 'B':(-1, 0), 'T':(1,0), 'RT':(1,1), 'LT':(1, -1), 'RB':(-1, 1), 'LB':(-1, -1)}

kx, ky = location[king[0]], int(king[1])-1
rx, ry = location[rock[0]], int(rock[1])-1

arr[ky][kx] = 'K'
arr[ry][rx] = 'R'


for _ in range(N):
    lo = input().rstrip()
    # print(moving[lo])

    dy, dx = moving[lo]

    ky, kx = ky + dy, kx + dx

    # 킹이 돌과 같은 방향으로 움직일때
    if ky == ry and kx == rx:

        ry, rx = ry + dy, rx + dx
        # 킹과 돌 모두 인덱스 아웃 되면 안됨
        if 0 <= ky < 8 and 0 <= kx < 8 and 0 <= ry < 8 and 0 <= rx < 8:
            arr[ky-dy][kx-dx] = 0
            arr[ry-dy][rx-dx] = 0

            arr[ky][kx] = 'K'
            arr[ry][rx] = 'R'

        # 인덱스 아웃 발생시 다시 제자리
        else:
            ky, kx = ky-dy, kx-dx
            ry, rx = ry-dy, rx-dx

    # 킹과 돌이 같은 방향이 아닐때
    else:
        # 범위 내
        if 0 <= ky < 8 and 0 <= kx < 8:
            arr[ky - dy][kx - dx] = 0
            arr[ky][kx] = 'K'
        # 범위 외
        else:
            ky, kx = ky - dy, kx - dx


for i in range(8):

    if 'K' in arr[i]:
        kx, ky = arr[i].index('K'), i+1
    if 'R' in arr[i]:
        rx, ry = arr[i].index('R'), i+1

print(f'{location_t[kx]}{ky}')
print(f'{location_t[rx]}{ry}')
