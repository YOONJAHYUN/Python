import sys

input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(19)]
# 검은 바둑 1 흰 바둑 2

# for i in data:
#     print(i)
di = [0, 1, 1, 1] # 세로
dj = [1, 0, 1, -1] #가로
result = 0
for i in range(19):
    for j in range(19):
        if data[i][j] != 0:
            # 하나씩 순회하다가 검은돌을 만남
            count1 = 0
            group1 = []
            count2 = 0
            group2 = []
            if data[i][j] == 1:
                group1.append((i+1,j+1))
                count1 += 1
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 근처를 순회해서 그 방향으로 검은돌을 찾는다.
                    if 0 <= ni < 19 and 0 <= nj < 19 and data[ni][nj] == 1:
                        if 0 <= i-di[k] < 19 and 0 <= j-dj[k] < 19 and data[i-di[k]][j-dj[k]] == 1:
                            break

                        else:
                            while True:
                                if 0 <= ni < 19 and 0 <= nj < 19 and data[ni][nj] == 1:
                                    group1.append((ni + 1, nj + 1))
                                    count1 += 1
                                    ni = ni + di[k]
                                    nj = nj + dj[k]
                                else:
                                    if count1 == 5:
                                        print(1)
                                        group1.sort(key=lambda x: (x[1], x[0]))
                                        print(*group1[0])
                                        result = 1
                                        break
                                    else:
                                        group1 = []
                                        group1.append((i+1,j+1))
                                        count1 = 1
                                        break


            elif data[i][j] == 2:
                count2 += 1
                group2.append((i + 1, j + 1))
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    # 근처를 순회해서 그 방향으로 하얀돌을 찾는다.
                    if 0 <= ni < 19 and 0 <= nj < 19 and data[ni][nj] == 2:
                        if 0 <= i-di[k] < 19 and 0 <= j-dj[k] < 19 and data[i-di[k]][j-dj[k]] ==2:
                            break

                        else:
                            while True:
                                if 0 <= ni < 19 and 0 <= nj < 19 and data[ni][nj] == 2:
                                    count2 += 1
                                    group2.append((ni + 1, nj + 1))
                                    ni = ni + di[k]
                                    nj = nj + dj[k]
                                else:
                                    if count2 == 5:
                                        print(2)
                                        group2.sort(key=lambda x: (x[1], x[0]))
                                        print(*group2[0])
                                        result = 1
                                        break
                                    else:
                                        group2 = []
                                        group2.append((i+1,j+1))
                                        count2 = 1
                                        break


else:
    if result == 0:
        print(0)
