import sys
input = sys.stdin.readline

# 가로 체크
def check1(y, x, num):
    for number in data[y]:
        if number == num:
            return False

    return True

# 세로체크
def check2(y, x, num):

    for i in range(9):
        if data[i][x]== num:
            return False

    return True

# 3*3 체크
def check3(y, x, num):
    for i in range(3):
        for j in range(3):
            if data[(y//3)*3 + i][(x//3)*3 + j] == num:
                return False

    return True


def check(now):

    if now == len(lst):
        for i in data:
            print(*i)
        # return
        exit(0)
    else:
        y, x = lst[now]
        for num in range(1, 10):
            if check1(y, x, num) and check2(y, x, num) and check3(y, x, num):
                data[y][x] = num
                # print(y, x, num)
                check(now+1)
                data[y][x] = 0



data = [list(map(int, input().split())) for _ in range(9)]

lst = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            lst.append((i, j))

check(0)

