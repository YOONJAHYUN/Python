import sys
from copy import deepcopy
input = sys.stdin.readline

def fish_move(arr,fish_location, fish_dir, sharkY,sharkX, shark_dir, shark_eat):
    # print("^&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"*30)
    # print(sharkY, sharkX, shark_dir, shark_eat)
    # for i in arr:
    #     print(i)
    # print("####################"*30)

    for now in range(1, 17):
        # 잡아먹힌게 아니라면
        if fish_location[now] != (-1, -1):

            orgin_dir = fish_dir[now]
            y, x = fish_location[now]

            while True:
                dy, dx = move[fish_dir[now]]

                # 교환할 친구
                ny, nx = y+dy, x+dx

                # 범위안에 있고 이게 상어위치랑 다르다면
                if 0 <= ny < 4 and 0 <= nx < 4 and (sharkY != ny or sharkX != nx):
                    # 자리를 교환한다.
                    arr[ny][nx], arr[y][x] = arr[y][x], arr[ny][nx]
                    # 빈자리가 아닌 경우
                    if arr[y][x]:
                        fish_location[arr[y][x]] = (y, x)
                    fish_location[now] = (ny, nx)

                    break
                # 범위 밖이거나 상어 위치라면?
                else:
                    fish_dir[now] += 1

                    if fish_dir[now] == 9:
                        fish_dir[now] = 1

                    if orgin_dir == fish_dir[now]:
                        break


    # print(fish_dir)
    # print(fish_location)
    # print("####################"*30)
    shark_move(arr, fish_location, fish_dir, sharkY, sharkX, shark_dir, shark_eat)

def shark_move(arr,fish_location, fish_dir, sharkY,sharkX, shark_dir, shark_eat):
    global answer
    # print(fish_location, fish_dir, sharkY,sharkX, shark_dir, shark_eat)
    dy, dx = move[shark_dir]

    for mul in range(1, 5):
        ny = sharkY + dy*mul
        nx = sharkX + dx*mul

        # 상어의 이동이 범위 안에 있고 물고기가 있다면
        if 0 <= ny < 4 and 0 <= nx < 4 and arr[ny][nx]:
            # 물고기를 먹는다.
            fish = arr[ny][nx]

            fish_location[fish] = (-1, -1)
            arr[ny][nx] = -1
            arr[sharkY][sharkX] = 0
            fish_move(deepcopy(arr),deepcopy(fish_location), deepcopy(fish_dir), ny, nx, fish_dir[fish], shark_eat+fish)
            # 다시 돌리기
            arr[sharkY][sharkX] = -1

            arr[ny][nx] = fish
            fish_location[fish] = (ny, nx)

    else:
        answer = max(shark_eat, answer)
        return


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
fish_location = [(0, 0)] * 17
fish_dir = [0] * 17
answer = 0
for i in range(4):
    temp = list(map(int, input().split()))
    lst = []
    for j in range(0, 8, 2):
        fish_dir[temp[j]] = temp[j+1]
        fish_location[temp[j]] = (i, j//2)
        lst.append(temp[j])
    arr.append(lst)

sharkX, sharkY = 0, 0
shark_eat = arr[0][0]
shark_dir = fish_dir[arr[0][0]]
fish_location[arr[0][0]] = (-1, -1)

arr[0][0] = -1


fish_move(arr,fish_location, fish_dir, sharkY,sharkX, shark_dir, shark_eat)

print(answer)