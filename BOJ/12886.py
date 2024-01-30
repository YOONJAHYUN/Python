import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 3의 배수가 되지 않으면 성립되지 않음
TOTAL = a + b + c

if TOTAL % 3:
    print(0)

else:
    visited = [[False]*TOTAL for _ in range(TOTAL)]
    q = deque()

    q.append((a, b))
    visited[a][b] = True

    while q:

        A, B = q.popleft()
        C = TOTAL - (A+B)

        if A == B == C:
            print(1)
            exit()

        for X, Y in ((A, B), (A, C), (B, C)):
            if X == Y:
                continue

            if X > Y:
                X, Y = Y, X

            X, Y = X + X, Y - X

            my_min = min(X, Y, TOTAL-(X+Y))
            my_max = max(X, Y, TOTAL-(X+Y))

            if visited[my_min][my_max]:
                continue
            q.append((my_min, my_max))
            visited[my_min][my_max] = True

    print(0)


