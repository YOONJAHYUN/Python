import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())

    original = []
    stack = []
    for _ in range(K):
        x, y = map(int, input().split())
        original.append((x, y))
        stack.append((x, y))

    for nx, ny in original:
        for i in range(2):
            if 0 <= nx+dx[i] < M and 0 <= ny+dy[i] < N:
                if (nx+dx[i], ny+dy[i]) in original:
                    if (nx+dx[i], ny+dy[i]) in stack:
                        idx = stack.index((nx+dx[i], ny+dy[i]))
                        stack.pop(idx)
                    else:
                        if (nx, ny) in stack:
                            idx = stack.index((nx, ny))
                            stack.pop(idx)
    print(stack)
    print(len(stack))