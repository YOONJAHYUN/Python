import sys
from collections import deque
sys.stdin = open('input.txt')

for tc in range(1, 11):

    n, start = map(int, input().split())

    data = list(map(int, input().split()))

    node = [[]*101 for _ in range(101)]

    for i in range(n//2):
        v1, v2 = data[i*2], data[i*2+1]
        node[v1].append(v2)

    visited = [0] *101

    stack = deque()
    stack.append(start)
    visited[start] = 1

    while stack:

        call = stack.popleft()

        for i in node[call]:
            if not visited[i]:
                stack.append(i)
                visited[i] = visited[call] + 1

    # print(visited)
    my_maxx = max(visited)

    for i in range(101):
        if visited[i] == my_maxx:
            my_max = i

    print(f'#{tc}', my_max)
