import sys
from collections import deque

input = sys.stdin.readline

a, b, c = map(int, input().split())

# 3의 배수가 되지 않으면 성립되지 않음
if (a + b + c) % 3:
    print(0)
elif a == b == c:
    print(1)
else:
    visited = [[[False for _ in range(501)] for _ in range(501)] for _ in range(501)]

    q = deque()

    q.append((a, b, c))

    flag = False

    while q:

        A, B, C = q.popleft()

        if A == B == C:
            # print(1)
            flag = True
            break

        rock = [A, B, C]

        rock.sort()

        if not visited[rock[0]][rock[1]][rock[2]]:

            visited[rock[0]][rock[1]][rock[2]] = True

            if rock[0] != rock[2] and rock[0] + rock[0] <= 500 and rock[2] - rock[0] > 0 and len(set(rock[0] + rock[0], rock[2] - rock[0], rock[1])) == 3:
                q.append((rock[0] + rock[0], rock[2] - rock[0], rock[1]))
            if rock[0] != rock[1] and rock[0] + rock[0] <= 500 and rock[1] - rock[0] > 0 and len(set(rock[0] + rock[0], rock[1] - rock[0], rock[2])) == 3:
                q.append((rock[0] + rock[0], rock[1] - rock[0], rock[2]))
            if rock[1] != rock[2] and rock[1] + rock[1] <= 500 and rock[2] - rock[1] > 0 and len(set(rock[1] + rock[1], rock[2] - rock[1], rock[0])) == 3:
                q.append((rock[1] + rock[1], rock[2] - rock[1], rock[0]))

    if flag:
        print(1)
    else:
        print(0)