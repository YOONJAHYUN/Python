import sys
input = sys.stdin.readline

def choose(hubo, y, x):

    if hubo == False:
        return

    hubo = list(hubo)
    n = len(hubo)
    for i in range(n):
        data[y][x] = hubo[i]
        return

        # for j in range(9):
        #     for k in range(9):
        #         if data[j][k] == 0:
        #             Sudoku(j, k)
        #             break

        data[y][x] = 0
    # else:
    #     return


def Sudoku(y, x):

    # 가로줄 리스트
    lst1 = set(data[y])

    # lst1과 numbers의 차집합을 찾는다.
    hubo1 = numbers - lst1
    # print(hubo1)
    # 교집합이 한개인 경우 그게 정답
    if len(hubo1) == 1:
        # hubo1 = list(hubo1)
        # data[y][x] = hubo1[0]
        return list(hubo1)

    lst2 = []
    # 교집합이 한개 이상인 경우 세로줄도 탐색하기
    for i in range(9):
        lst2.append(data[i][x])

    # 세로줄 찾은 후 후보값 찾는다.
    hubo2 = numbers - set(lst2)

    if len(hubo2) == 1:
        # hubo2=list(hubo2)

        # data[y][x] = hubo2[0]
        return list(hubo2)
    # 후보 2도 여러개 인경우, 후보 1과 비교

    hubo3 = hubo1 & hubo2

    # hubo3의 길이
    if len(hubo3) == 1:
        # hubo3 = list(hubo3)
        # data[y][x] = hubo3[0]
        return list(hubo3)

    lst3 = []
    # 후보 3 도 여러개다... 그렇다면 3*3을 하자.
    for i in range((y//3)*3, (y//3)*3 + 3):
        for j in range((x//3)*3, (x//3)*3 +3):
            lst3.append(data[i][j])

    hubo4 = numbers - set(lst3)

    hubo5 = hubo3 & hubo4

    if hubo5:
        return hubo5

    else:
        return False


data = [list(map(int, input().split())) for _ in range(9)]

# 0 찾기
# 가로 세로 3*3 배열에서 교집합 찾기
numbers = set(range(1, 10))
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            # 후보를 찾아온다.
            # print(Sudoku(i, j))
            # 후보를 하나씩 넣어서 결과가 제대로 도출되는 지 확인. 만약 결과가 제대로 나오는지 확인
            # 만약 결과가 제대로 나오지 않는다면 다음값으로 넣기..
            choose(Sudoku(i,j), i, j)



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

'''