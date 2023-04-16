import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
'''
dir
0 -> 우
1 -> 하
2 -> 좌
3 -> 상
'''
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def snake(y, x, d, cnt, tail):


    # 뱀의 이동
    ny = y + dir[d][0]
    nx = x + dir[d][1]

    # 보드 나간경우
    if 0 > ny or ny >= N or 0 > nx or nx >= N:
        print(cnt)
        return
    # 뱀이 이미 있는 경우
    if data[ny][nx] == 1:
        print(cnt)
        return

    # 사과가 있는 경우
    if data[ny][nx] == -1:
        # 사과 먹기
        data[ny][nx] = 1
        tail.append((ny, nx))
    else:
        data[ny][nx] = 1
        tail.append((ny, nx))
        dy, dx = tail.pop(0)
        data[dy][dx] = 0

    # second 체크
    if second[cnt] == 'D':
        snake(ny, nx, (d+1)%4, cnt + 1, tail)

    elif second[cnt] == 'L':
        snake(ny, nx, (d-1)%4, cnt + 1, tail)
    else:
        snake(ny, nx, d, cnt+1, tail)


# 보드의 크기
N = int(input())
# 사과의 개수
K = int(input())

data = [[0] * N for _ in range(N)]
data[0][0] = 1
# 사과의 위치
for _ in range(K):
    y, x = map(int, input().split())
    # 사과 표기
    data[y-1][x-1] = -1

# 뱀의 방향 변환 횟수
L = int(input())
second = [0 for _ in range(10001)]
for _ in range(L):
    # x초
    # c == L 왼쪽 90도 회전
    # c == D 오른쪽 90도 회전
    x, c = input().split()
    x = int(x)
    second[x] = c

snake(0,0,0,1, [(0,0)])
'''
뱀
머리를 다음칸에 위치
그 칸에 사과가 있다면 꼬리는 그대로
그 칸에 사과가 없으면 꼬리가 사라짐

젤 처음 뱀은 0,0에서 오른쪽을 봄
'''
