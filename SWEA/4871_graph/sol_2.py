import sys

sys.stdin = open('input.txt')

def f(s, g):

    stack = []
    stack.append(s)

    while stack:

        start = stack.pop()
        visited[start] = True

        if start == g:
            return 1

        else:
            for i in data[start]:
                if visited[i] == False:
                    stack.append(i)

    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    data = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        data[a].append(b)
    # print(f'#{tc}', data)
    visited = [False for _ in range(V+1)]
    s, g = map(int, input().split())

    print(f'#{tc}', f(s,g))