import sys
from copy import deepcopy
input = sys.stdin.readline

def twozerofoureight(depth, data1, start):
    global ans

    if depth == 5:
        # print("도달")

        # print(start)
        # for i in data1:
        #     print(i)
        # print("#####################")
        for i in data1:
            ans = max(ans, max(i))
        return

    '''
    상 방향
    
    하나하나 해서 위에 블록이 없을때까지 블록을 위로 위치시킨다.
    블록이 있다면, 본인과 같은 블록이면 *2처리를 해줌
    아니라면, 그냥 그 자리에 위치시킨다. 
    '''

    data = deepcopy(data1)
    check = [[False] *n for _ in range(n)]

    for i in range(1, n):
        for j in range(n):
            # 블록이 있다면
            if data[i][j]:
                y = i - 1
                while y >= 0 and y < n:
                    # 본인보다 위에 블록이 있다면
                    if 0 <= y < n and data[y][j]:
                        # 나와 같다면?
                        if data[y][j] == data[i][j] and not check[y][j]:
                            # 2배를 해준다
                            data[y][j] *= 2
                            data[i][j] = 0
                            check[y][j] = True

                        # 나와 다르다면?
                        else:
                            # 거기에 멈춰
                            data[y+1][j] = data[i][j]
                            if y+1 != i:
                                data[i][j] = 0
                        break
                    # 블록이 없다면? 계속 위로 올라가기
                    y -= 1

                    if y == -1:
                        data[y + 1][j] = data[i][j]
                        data[i][j] = 0

    twozerofoureight(depth+1, data, start +"위 ")
    data = deepcopy(data1)
    check = [[False] *n for _ in range(n)]

    # 하
    for i in range(n-2, -1, -1):
        for j in range(n):
            # 블록이 있다면
            if data[i][j]:
                y = i + 1
                while y >= 0 and y <n:
                    # 본인보다 위에 블록이 있다면
                    if 0 <= y < n and data[y][j]:
                        # 나와 같다면?
                        if data[y][j] == data[i][j] and not check[y][j]:
                            # 2배를 해준다
                            data[y][j] *= 2
                            data[i][j] = 0
                            check[y][j] = True
                        # 나와 다르다면?
                        else:
                            # 거기에 멈춰
                            data[y-1][j] = data[i][j]

                            if y-1 != i:
                                data[i][j] = 0
                        break
                    # 블록이 없다면? 계속 위로 올라가기
                    y += 1
                    if y == n:
                        data[y - 1][j] = data[i][j]
                        data[i][j] = 0

    twozerofoureight(depth+1, data, start+"아래 ")
    data = deepcopy(data1)
    check = [[False] *n for _ in range(n)]


    # 좌
    for j in range(1, n):
        for i in range(n):
            # 블록이 있다면
            if data[i][j]:
                x = j - 1
                while x >= 0 and x <n:
                    # 본인보다 위에 블록이 있다면
                    if 0 <= x < n and data[i][x]:
                        # 나와 같다면?
                        if data[i][x] == data[i][j] and not check[i][x]:
                            # 2배를 해준다
                            data[i][x] *= 2
                            data[i][j] = 0
                            check[i][x] = True

                        # 나와 다르다면?
                        else:
                            # 거기에 멈춰
                            data[i][x+1] = data[i][j]

                            if x+1 != j:
                                data[i][j] = 0

                        break
                    # 블록이 없다면? 계속 위로 올라가기
                    x -= 1
                    if x == -1:
                        data[i][x+1] = data[i][j]
                        data[i][j] = 0
    twozerofoureight(depth+1, data, start+"왼쪽 ")
    data = deepcopy(data1)
    check = [[False] *n for _ in range(n)]


    # 우

    for j in range(n-2, -1, -1):
        for i in range(n):
            # 블록이 있다면
            if data[i][j]:
                x = j + 1
                while x >= 0 and x <n:
                    # 본인보다 위에 블록이 있다면
                    if 0 <= x < n and data[i][x]:
                        # 나와 같다면?
                        if data[i][x] == data[i][j] and not check[i][x]:
                            # 2배를 해준다
                            data[i][x] *= 2
                            data[i][j] = 0
                            check[i][x] = True


                        # 나와 다르다면?
                        else:
                            # 거기에 멈춰
                            data[i][x-1] = data[i][j]
                            if x-1 != j:
                                data[i][j] = 0

                        break
                    # 블록이 없다면? 계속 위로 올라가기
                    x += 1
                    if x == n:
                        data[i][x-1] = data[i][j]
                        data[i][j] = 0

    twozerofoureight(depth+1, data, start+"오른쪽 ")
    # data = deepcopy(data1)


n = int(input())
ans = 0
data = [list(map(int, input().split())) for _ in range(n)]
twozerofoureight(0, data, "")

print(ans)
'''
최대 5번 이동시켜 얻을 수 있는 가장 큰 블록 출력

그냥 무작정 상하좌우 돌리고..
최댓값 갱신하자.
'''