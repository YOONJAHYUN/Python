import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
jump = [[0]*N for _ in range(N)]
# print(data)
# 시작점

q = deque()
q.append((0, 0, data[0][0]))
jump[0][0] = 1
# cnt = 0
while q:
    dx, dy, distance = q.popleft()

    if distance == 0:
        continue
    # 범위 안에 들어있다.
    if 0 <= dx+distance < N and 0 <= dy < N:
        # 방문한 곳이 아닐경우
        if jump[dx+distance][dy] == 0:
            # 근데 거기가 도착지다?
            if dx + distance == N-1 and dy == N-1:
                # 원래 있던 곳을 더함
                jump[dx + distance][dy] = jump[dx][dy]

            # 도착지가 아닌 다른 곳이다.
            else:
                # q에 넣어준다.
                q.append((dx+distance, dy, data[dx+distance][dy]))
                # 방문 표시를 해준다.
                jump[dx+distance][dy] = jump[dx][dy]

        # 방문했던 곳이다.
        else:
            # 근데 거기가 도착지다?
            if dx + distance == N - 1 and dy == N - 1:
                # 도착지까지 올 수 있는 경우의 수를 더한다.
                jump[dx + distance][dy] += jump[dx][dy]
            # 거기가 도착지가 아니다?
            else:
                # 기록만 더 해준다.
                jump[dx+distance][dy] += jump[dx][dy]

    if 0 <= dx < N and 0 <= dy + distance < N:
        if jump[dx][dy + distance] == 0:
            if dx == N-1 and dy + distance == N-1:
                jump[dx][dy + distance] = jump[dx][dy]

            else:
                q.append((dx, dy + distance, data[dx][dy + distance]))
                jump[dx][dy + distance] = jump[dx][dy]

        else:
            if dx == N-1 and dy + distance == N-1:
                jump[dx][dy+distance] += jump[dx][dy]
            else:
                jump[dx][dy+distance] += jump[dx][dy]

# print(jump[-1][-1])

for i in jump:
    print(i)


'''
4
1 2 2 3
1 1 3 3
3 1 1 3
3 2 1 0
'''