import sys
input = sys.stdin.readline

def ladder(depth, arr):
    global answer

    if answer < depth:
        return

    if check(arr):
        answer = min(depth, answer)

    if depth == 3:
        return

    for i in range(h):
        for j in range(1, n):
            if not arr[i][j] and not arr[i][j+1]:
                arr[i][j], arr[i][j+1] = 1, 2
                ladder(depth+1, arr)
                arr[i][j], arr[i][j+1] = 0, 0


def check(arr):

    for j in range(1, n + 1):
        y = 0
        x = j
        while True:
            if y == h:
                if x != j:
                    return False
                break

            if arr[y][x] == 1:
                x += 1
            elif arr[y][x] == 2:
                x -= 1
            y += 1

    return True

# n 세로선 m 가로선 h 위치의 개수
n, m, h = map(int, input().split())

arr = [[0] * (n+1) for _ in range(h+1)]
answer = 4
# b 번 세로선 b+1번 세로선을 a번 점선에서 연결 (a번 가로선)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b] = 1
    arr[a-1][b+1] = 2



ladder(0, arr)
#
print(answer if answer < 4 else -1)
