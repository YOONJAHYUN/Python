import sys
from collections import deque
input = sys.stdin.readline

# 수빈이 N 동생 K
N, K = map(int, input().split())

# 걸으면 1칸(X+1)or (X-1) 순간이동은 2*X
# 너비탐색으로 가면 될 것 같다.
# 5에서 시작하면, 4, 6, 10으로 나뉘고 또 이게 막 늘어남..
# 근데 생각해보니까 N과 K가 100,000이전이니까 걍 리스트 만들어서 해보자

dot = [-1] *(100001)
# print(dot)

q = deque()

dot[N] = 0
q.append(N)
while True:
    move = q.popleft()

    if move == K:
        print(dot[move])
        break


    if 0 <= move-1 < 100001 and dot[move-1] == -1:
        q.append(move-1)
        dot[move-1] = dot[move] + 1

    if 0 <= move+1 < 100001 and dot[move + 1] == -1:
        q.append(move+1)
        dot[move+1] = dot[move] + 1

    if 0 <= move*2 < 100001 and dot[move * 2] == -1:
        q.append(move*2)
        dot[move*2] = dot[move] + 1



