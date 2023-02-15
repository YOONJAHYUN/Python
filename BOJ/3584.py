import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    node = [[] for _ in range(N+1)]
    for i in range(N-1):
        A, B = map(int, input().split())

        node[B].append(A)

    s, g = map(int, input().split())

    stack1 = []
    stack1.append(s)
    stack2 = []
    stack2.append(g)
    visited1 = []
    visited2 = []
    while True:
        if stack1:
            s = stack1.pop()
            visited1.append(s)
        if stack2:
            g = stack2.pop()
            visited2.append(g)

        if g in visited1:
            print(g)
            break
        elif s in visited2:
            print(s)
            break

        else:
            # stack1.append(*node[s])
            # stack2.append(*node[g])
            if node[s] and node[g]:
                stack1.append(*node[s])
                stack2.append(*node[g])
            elif node[s] and not node[g]:
                stack1.append(*node[s])
            elif node[g] and not node[s]:
                stack2.append(*node[g])