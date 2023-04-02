import sys
input = sys.stdin.readline

def checkRow(x, a):
    for i in range(9):
        if a == data[x][i]:
            return False
    else:
        return True

def checkCol(y, a):
    for i in range(9):
        if a == data[i][y]:
            return False
    else:
        return True

def checkRect(x,y,a):
    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (y//3)*3+3):
            if a == data[i][j]:
                return False
    else:
        return True

def dfs(idx):
    if idx == len(blank):
        for i in data:
            print(*i)
        exit(0)

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x,y,i):
            data[x][y] = i
            dfs(idx+1)
            data[x][y] = 0


data = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            blank.append([i,j])

dfs(0)
