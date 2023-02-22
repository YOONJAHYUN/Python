import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

color0 = 0
color1 = 0

def cut_paper(x, y, n):
    global color0, color1

    cnt0 = 0
    cnt1 = 0
    for i in range(y, y+n):
        for j in range(x, x+n):
            if paper[i][j] == 0:
                cnt0 += 1
            else:
                cnt1 += 1

    if cnt0 == n*n:
        color0 += 1

    elif cnt1 == n*n:
        color1 += 1

    else:
        cut_paper(x, y, n//2)
        cut_paper(x+n//2, y, n // 2)
        cut_paper(x, y+n//2, n // 2)
        cut_paper(x+n//2, y+n//2, n // 2)


cut_paper(0, 0, N)

print(color0)
print(color1)