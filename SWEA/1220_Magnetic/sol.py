import sys
# sys.stdin = open('input.txt')

for tc in range(1, 2):
    # n 정사각형 테이블의 한 변의 길이
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(7)]

    # 1은 N극 2는 S극
    # N과 S를 세로 단위로 따로 모은다.
    table = [[] for _ in range(7)]

    for j in range(7):
        for i in range(7):
            if data[i][j] != 0:
                table[j].append(data[i][j])
    # print(table)
    cnt = 0

    for i in range(7):
        N_count = 0
        S_count = 0
        while True:
            if table[i] and table[i][0] == 2:
                table[i].pop(0)

            if table[i] and table[i][-1] == 1:
                table[i].pop()

            if not table[i]:
                break

            if len(table[i])>=2 and table[i][0] == 1 and table[i][-1] == 2:
                # print(table[i])

                N_count += table[i].count(1)
                S_count += table[i].count(2)
                print(i, table[i])
                break
        cnt += min(N_count, S_count)
    print(f'#{tc}', cnt)



'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''

'''
7
1 1 1 1 1 1 1
'''


