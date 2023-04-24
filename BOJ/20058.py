import sys
input = sys.stdin.readline
from collections import deque

def turn(x, y, k, n):

    if k == n:
        my_new = []
        for j in range(y, y+n):
            temp = []
            for i in range(x, x+n):
                temp.append(data[i][j])
            my_new.append(temp[::-1])

        for i in range(n):
            for j in range(n):
                new[i+x][j+y] = my_new[i][j]
        return

    else:
        turn(x, y, k, n//2)
        turn(x, y+n//2, k, n//2)
        turn(x+n//2, y, k, n//2)
        turn(x+n//2, y+n//2, k, n//2)


def magic(num):

    # 격자나눠 회전
    turn(0, 0, num, n)
    dir = [(0,-1),(0,1),(1,0),(-1,0)]
    magicshop = []
    # 그리고 체크
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(4):
                ni = i + dir[k][0]
                nj = j + dir[k][1]
                if 0 <= ni < n and 0 <= nj < n:
                    if new[ni][nj] > 0:
                        count += 1
            if count < 3:
                magicshop.append((i, j))

    for i, j in magicshop:
        if new[i][j] > 0:
            new[i][j] -= 1

    # dir로 상하좌우 조사
    # 그 리스트를 반환
def bfs():
    my_max = 0
    q = deque()
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if data[i][j] > 0 and not visited[i][j]:
                idx = 1
                q.append((i, j))
                visited[i][j] = idx
                idx += 1
                while q:

                    ni, nj = q.popleft()

                    for di, dj in ((-1,0), (1, 0), (0, 1), (0, -1)):
                        si, sj = ni+di, nj+dj
                        if 0 <= si < n and 0 <= sj < n and not visited[si][sj] and data[si][sj]>0:
                            q.append((si, sj))
                            visited[si][sj] = idx
                            my_max = max(my_max, idx)
                            idx += 1

    return my_max



N, Q = map(int, input().split())
n = 2**N
data = [list(map(int, input().split())) for _ in range(n)]

L = list(map(int, input().split()))

'''
격자를 2**L * 2**L 크기로 나눔
그리고 모든 부분을 시계방향으로 90도 회전
인접한칸 카운트해서 3개이상이 얼음이 있어야됨
없으면 얼음 -1
'''

'''
1. 격자의 크기를 나눈다.
분할정복을 사용한다.
2. 회전시키고
3. 회전시킨상태에서 얼음체크
'''

for i in range(Q):
    cnt = 2**L[i]
    new = [[0] * n for _ in range(n)]
    magic(cnt)
    data = new

ice = 0
for j in range(n):
    for k in range(n):
        if data[j][k]> 0:
            ice += data[j][k]

print(ice)
print(bfs())

