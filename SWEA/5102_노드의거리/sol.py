import sys

sys.stdin = open('input.txt')

T = int(input())

def bfs(s, g):
    q.append(s)
    visited[s] = 0
    while q:
        n = q.pop(0)

        if n == g:
            print(f'#{tc}', visited[g])
            break
        else:
            for i in node[n]:
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[n] + 1

    else:
        print(f'#{tc}', 0)


for tc in range(1, T+1):
    V, E = map(int, input().split())

    node = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        node[v1].append(v2)
        node[v2].append(v1)
    # print(node)
    S, G = map(int, input().split())
    # print(f'#{tc}', S, G)
    visited = [-1] * (V+1)
    q = []
    bfs(S, G)
    # print(visited)
