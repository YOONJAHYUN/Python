import sys

sys.stdin = open('input.txt')

T = int(input())





for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = list(range(1, 10))
    # print(result)
    new_arr = []
    for i in range(9):
        new = []
        for j in range(9):
            new.append(arr[j][i])
        new_arr.append(new)

    new_new_arr = []
    for i in range(0, 9, 3):

        for j in range(0, 9,3):
            new = []
            for k in range(0, 3):
                for l in range(0, 3):
                    new.append(arr[i+k][j+l])
            new_new_arr.append(new)


    while True:
        count = 0
        for i in range(9):
            arr[i].sort()
            if arr[i] == result:
                continue
            else:
                count += 1

        if count >= 1:
            print(f'#{tc}', 0)
            break

        for i in range(9):
            new_arr[i].sort()
            if new_arr[i] == result:
                continue
            else:
                count += 1

        if count >= 1:
            print(f'#{tc}', 0)
            break

        for i in range(9):
            new_new_arr[i].sort()
            if new_new_arr[i] == result:
                continue
            else:
                count += 1
        if count >= 1:
            print(f'#{tc}', 0)
            break

        else:
            print(f'#{tc}', 1)
            break
