import sys

input = sys.stdin.readline

def color(idx, color_sum, depth):
    global my_color
    if depth == N:
        my_color = min(color_sum, my_color)
        return

    for j in range(3):

        if color_sum > my_color:
            return

        if depth == 0:
            select[depth][j] = True
            color(idx + 1, color_sum + data[depth][j], depth + 1)
            select[depth][j] = False

        elif depth != 0 and not select[depth-1][j]:
            select[depth][j] = True
            color(idx + 1, color_sum + data[depth][j], depth+1)
            select[depth][j] = False


N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

select = [[False]*3 for _ in range(N)]
# print(select)
my_color = N*1000
color(0, 0, 0)

print(my_color)

