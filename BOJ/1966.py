import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    docu = deque()
    important = list(map(int, input().split()))
    # print(important)

    for i in range(N):
        docu.append((i, important[i]))


    # print(docu)

    # M이 인덱스니까 docu에서 M인덱스 값을 찾고, 그 값보다 큰 애들을 먼저 빼준다.
    imp = docu[M][1]

    num = 0
    # 우선순위 높은 것 부터 빼주자

    while True:

        my_max = 0
        for i, j in docu:
            my_max = max(j, my_max)

        a, b = docu.popleft()
        if b < my_max:
            docu.append((a, b))

        else:
            if imp < b:
                num += 1
                continue

            elif imp > b:
                docu.append((a, b))

            else:
                if a == M:
                    num += 1
                    print(num)
                    break
                else:
                    num += 1


''''''
# q랑 idx 돌리는거거
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            pop_idx = idx.popleft()
            if pop_idx == m:
                print(cnt)
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
''''''