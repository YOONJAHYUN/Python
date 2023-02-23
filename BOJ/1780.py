import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

color_a = 0
color_b = 0
color_c = 0

def paper_cut(x, y, n):
    global color_a, color_b, color_c
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0

    for i in range(y, y+n):
        for j in range(x, x+n):
            if paper[i][j] == -1:
                cnt_a += 1
            elif paper[i][j] == 0:
                cnt_b += 1
            elif paper[i][j] == 1:
                cnt_c += 1

    if cnt_a == n**2:
        color_a += 1

    elif cnt_b == n**2:
        color_b += 1

    elif cnt_c == n**2:
        color_c += 1

    else:
        paper_cut(x, y, n//3)

        paper_cut(x+n//3, y, n // 3)
        paper_cut(x+(n//3)*2, y, n // 3)

        paper_cut(x, y+n//3, n // 3)
        paper_cut(x, y+(n//3)*2, n // 3)

        paper_cut(x+n//3, y+n//3, n // 3)
        paper_cut(x+n//3, y+(n//3)*2, n // 3)

        paper_cut(x+(n//3)*2, y+(n//3)*2, n // 3)
        paper_cut(x+(n//3)*2, y+n//3, n // 3)

paper_cut(0, 0, N)

print(color_a)
print(color_b)
print(color_c)