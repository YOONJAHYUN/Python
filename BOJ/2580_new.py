import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def sudoku(num, y, x, idx, n):

    if num >= 10:
        return

    # 가로줄 검사
    if num in data[y]:
        # 가로줄에 num 있으면 숫자 늘리기
        sudoku(num+1, y, x, idx, n)
        sudoku(num+2, y, x, idx, n)
        sudoku(num+3, y, x, idx, n)
        sudoku(num+4, y, x, idx, n)
        sudoku(num+5, y, x, idx, n)
        sudoku(num+6, y, x, idx, n)
        sudoku(num+7, y, x, idx, n)
        sudoku(num+8, y, x, idx, n)

        return
    # 가로줄에 없는 숫자임
    # 세로줄 검사
    else:
        for i in range(9):
            if data[i][x] == num:
                sudoku(num + 1, y, x, idx, n)
                sudoku(num + 2, y, x, idx, n)
                sudoku(num + 3, y, x, idx, n)
                sudoku(num + 4, y, x, idx, n)
                sudoku(num + 5, y, x, idx, n)
                sudoku(num + 6, y, x, idx, n)
                sudoku(num + 7, y, x, idx, n)
                sudoku(num + 8, y, x, idx, n)
                return
        else:

            # 3* 3검사
            for i in range((y//3)*3, (y//3)*3+3):
                for j in range((x//3)*3, (x//3)*3+3):
                    if data[i][j] == num:
                        sudoku(num + 1, y, x, idx, n)
                        sudoku(num + 2, y, x, idx, n)
                        sudoku(num + 3, y, x, idx, n)
                        sudoku(num + 4, y, x, idx, n)
                        sudoku(num + 5, y, x, idx, n)
                        sudoku(num + 6, y, x, idx, n)
                        sudoku(num + 7, y, x, idx, n)
                        sudoku(num + 8, y, x, idx, n)
                        return
            else:
                data[y][x] = num
                # print(idx, num)

                if idx == n:
                    for i in data:
                        print(*i)
                    exit(0)
                else:
                    sudoku(1, blank[idx][0], blank[idx][1], idx+1, n)
                    return


data = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            blank.append([i,j])
N = len(blank)
sudoku(1, blank[0][0], blank[0][1], 1, N)
for i in data:
    print(*i)


'''
0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1


0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''
