import sys
input = sys.stdin.readline

'''
좌표갱신하면서 맥주남아잇으면 다음다음 그러다가 갱신
그러다가 페스티벌이면 굿

'''
def BFS(start):
    global flag
    sx, sy = start
    if abs(sy-ey) + abs(sx-ex) <= 1000:
        flag = True
        return

    for i in range(n):
        x, y = stores[i]
        if abs(sy-y) + abs(sx-x) <= 1000 and not visited[i]:
            visited[i] = True
            BFS((x, y))
            visited[i] = False


t = int(input())

for _ in range(t):
    n = int(input())
    flag = False
    # 집
    start = tuple(map(int, input().split()))
    stores = []

    # 편의점
    for _ in range(n):
        x, y = map(int, input().split())
        stores.append((x, y))
    visited = [False for _ in range(n)]

    # 페스티벌
    ex, ey = map(int, input().split())

    BFS(start)

    if flag:
        print('happy')
    else:
        print('sad')