import sys

input = sys.stdin.readline


def fish_moving():

    idx = 1
    while True:

        if idx > 16:
            break

        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == idx:

                    orgin_dir = arr[i][j][1]

                    while True:
                        dy, dx = move_dir[arr[i][j][1]]

                        ny, nx = dy+i, dx+j

                        if 0 <= ny < 4 and 0 <= nx < 4 and (ny != sharkY or nx != sharkX):
                            arr[i][j], arr[ny][nx] = arr[ny][nx], arr[i][j]
                            break
                        else:

                            arr[i][j][1] += 1

                            if arr[i][j][1] == 9:
                                arr[i][j][1] = 1

                            if orgin_dir == arr[i][j][1]:
                                break
                    break

        idx += 1


move_dir = [
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
for i in range(4):
    temp = list(map(int, input().split()))
    lst = []
    for j in range(0, 8, 2):
        lst.append([temp[j], temp[j+1]])
    arr.append(lst)

print(arr)

sharkX, sharkY = 0, 0
eat = arr[0][0][0]
sharkDir = arr[0][0][1]
arr[0][0] = [-1, sharkDir]
print(arr)
fish_moving()
for i in arr:
    print(*i)
# print(arr)

