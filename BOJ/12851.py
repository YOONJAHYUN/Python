import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

if K <= N:
    print(N-K)
    print(1)


else:
    visited = [-1] * 100001
    visited[N] = 0

    q = deque()
    q.append((N, 0))

    cnt = 0
    visit = -5

    while q:

        x, time = q.popleft()
        visited[x] = 0

        if time > visit and visit != -5:
            break

        if x == K:
            cnt += 1

        else:
            if 0 <= x * 2 <= 100000 and visited[x * 2] == -1:
                q.append((x * 2, time + 1))
                if x * 2 == K:
                    if visit == -5:
                        visit = time + 1

            if 0 <= x - 1 <= 100000 and visited[x - 1] == -1:
                q.append((x - 1, time + 1))
                if x - 1 == K:
                    if visit == -5:
                        visit = time + 1


            if 0 <= x + 1 <= 100000 and visited[x + 1] == -1:
                q.append((x + 1, time + 1))
                if x + 1 == K:
                    if visit == -5:
                        visit = time + 1

    print(visit)
    print(cnt)
