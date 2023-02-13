import sys

sys.stdin = open('input.txt')

T = int(input())

###############################################################
for tc in range(T):
    # s = [[0] * 9 for _ in range(9)]
    line = [list(map(int, input().split())) for _ in range(9)]

    # print(line)
###############################################################
    new_line = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            new_line[i][j] = line[8-j][i]


###############################################################
    new_new_line = [[] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            new_new_line[(i//3) * 3 + (j//3)].append(line[i][j])

    # print(new_new_line)



############################################################

    count = 0

    for i in range(9):
        if len(set(line[i])) == 9:
            continue
        else:
            count += 1
            break

    if count == 0:
        for i in range(9):
            if len(set(new_line[i])) == 9:
                continue
            else:
                count += 1
                break

    if count == 0:
        for i in range(9):
            if len(set(new_new_line[i])) == 9:
                continue
            else:
                count += 1
                break


    if count == 0:
        print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)


