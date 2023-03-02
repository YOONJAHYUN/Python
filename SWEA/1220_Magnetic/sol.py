import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # n 정사각형 테이블의 한 변의 길이
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    # 1은 N극 2는 S극
    # N과 S를 세로 단위로 따로 모은다.
    table = [[] for _ in range(100)]

    for i in range(100):        # 세로
        for j in range(100):    # 가로
            if data[99-i][j] != 0:
                table[j].append(data[99-i][j])

    cnt = 0

    for i in range(100):
        while True:
            if table[i] and table[i][0] == 1:
                table[i].pop(0)

            if table[i] and table[i][-1] == 2:
                table[i].pop()

            if not table[i]:
                break

            if len(table[i])>=2 and table[i][0] == 2 and table[i][-1] == 1:

                lst = []
                for i in table[i]:
                    if i == 1:
                        if lst and lst[-1] == 2:
                            cnt += 1
                            lst.append(i)
                        else:
                            lst.append(i)
                    else:
                        lst.append(i)

                # print(i, table[i])
                break

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


