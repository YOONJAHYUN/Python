import sys
from copy import deepcopy
input = sys.stdin.readline

'''
청소년 0,0 물고기 먹고 0,0 들어감
상어방향은 0,0 방향으로 변경

물고기 = 한 칸 이동, 
이동할 수 있는 칸 = 빈칸, 다른 물고기가 있는 칸
이동할 수 없는 칸 = 상어, 공간의 경계 넘기

방향이 이동할 수 있는 칸을 향할 때 까지 방향을 45도 반시계 회전
이동할 수 있는 칸 없으면 이동 안함

다른 물고기가 있는 방향은 서로의 위치를 바꾸는 방식
===================================================
물고기 이동 모두 끝나고 상어 이동
한번에 여러개 칸 가능
상어가 물고기 잇는 칸 => 물고기 먹기 그 방향 가지기
이동하는 중에 지나가는 칸에 있는 물고기 먹지않음
물고기가 없는 칸은 못감

상어가 이동할 수잇는 공간 업승면 집감
상어 이동 후 다시 물고기 이동

상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
'''

def fish_moving(sharkX, sharkY, shark, eat,arr, fish, fish_dir):

    for now in range(1, 17):
        # 아직 물고기가 살아있다면
        if fish[now]:
            y, x = fish[now]
            now_dir = [False] * 9
            now_dir[fish_dir[now]] = True

            while True:
                dy, dx = move[fish_dir[now]]
                ny, nx = y+dy, x+dx
                # 조건 안에 있고 그 위치에 상어가 없다면,
                if 0 <= ny < 4 and 0 <= nx < 4 and not (ny == sharkX and nx == sharkY):
                    # 상어 자리 교환한다.
                    arr[ny][nx], arr[y][x] = arr[y][x], arr[ny][nx]
                    # 이동된 자리 교환한다.
                    # 물고기가 있는 경우에만 이동
                    # if arr[y][x] != 0:
                    fish[now], fish[arr[y][x]] = fish[arr[y][x]], fish[now]
                    break
                # 자리 이동을 못하는 경우
                else:
                    # 방향을 변경해준다.
                    fish_dir[now] += 1

                    if fish_dir[now] == 9:
                        fish_dir[now] = 1

                    # 계속 방향을 변경한건데 또 맴돌았다면?
                    if now_dir[fish_dir[now]]:
                        break
                    else:
                        now_dir[fish_dir[now]] = True



    shark_moving(sharkX, sharkY, shark, eat,arr, fish, fish_dir)

def shark_moving(sharkX, sharkY, shark, eat,arr, fish, fish_dir):
    global answer
    dy, dx = move[shark]
    print(sharkX, sharkY, shark, eat, fish, fish_dir)

    for i in arr:
        print(i)
    print("####################")
    # x, y = sharkX, sharkY

    # copy_arr = deepcopy(arr)
    # copy_fish = deepcopy(fish)
    # copy_fish_dir = deepcopy(fish_dir)

    for mul in range(1, 5):
        ny = sharkY + dy*mul
        nx = sharkX + dx*mul

        if 0 <= ny < 4 and 0 <= nx < 4 and arr[ny][nx]:
            # 먹을 수 있는 물고기
            my_fish = arr[ny][nx]
            # 물고기 먹고 상어 이동
            arr[ny][nx] = -1
            # 원래 있던 자리 빈자리
            arr[sharkY][sharkX] = 0
            # 그 물고기 죽음
            fish[my_fish] = False
            # 다시 물고기 이동
            fish_moving(ny, nx, fish_dir[my_fish], eat+my_fish, deepcopy(arr), deepcopy(fish), deepcopy(fish_dir))
            # 원상복구
            fish[my_fish] = (ny, nx)
            arr[sharkY][sharkX] = -1
            arr[ny][nx] = my_fish


    else:
        answer = max(answer, eat)
        # return


move = [
    (0, 0),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
]

arr = []
fish = [(0, 0)] * 17
fish_dir = [0] * 17
for i in range(4):
    temp = list(map(int, input().split()))
    lst = []
    for j in range(0, 8, 2):
        fish_dir[temp[j]] = temp[j+1]
        fish[temp[j]] = (i, j//2)
        lst.append(temp[j])
    arr.append(lst)
# print("arr", arr)
# print("fish",fish)
# print("fish_dir",fish_dir)

answer = 0
# 첫 시작은 상어가 들어감
y, x = 0, 0
fish[arr[0][0]] = False
eat = arr[0][0]
shark, arr[0][0] = fish_dir[arr[0][0]], -1
# 물고기 이동
fish_moving(0, 0, shark, eat, deepcopy(arr), deepcopy(fish), deepcopy(fish_dir))
# print("arr", arr)
# print("fish",fish)
# print("fish_dir",fish_dir)

print(answer)