import sys

input = sys.stdin.readline

bing_go = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
bing = 0
for _ in range(5):
    let_s_bing = list(map(int, input().split()))

    for number in let_s_bing:

        for i in range(5):
            for j in range(5):
                if bing_go[i][j] == number:
                    bing_go[i][j] = 0
                    cnt += 1
                    break

        # 대각선 빙고
        daegak1 = 0
        daegak2 = 0
        for i in range(5):
            if bing_go[i][i] == 0:
                daegak1 += 1
            if bing_go[i][4-i] == 0:
                daegak2 += 1

        if daegak1 == 5:
            bing += 1
        if daegak2 == 5:
            bing += 1


        # 가로 빙고
        for i in range(5):
            if bing_go[i] == [0, 0, 0, 0, 0]:
                bing += 1

        # 세로 빙고
        for j in range(5):
            sero = 0
            for i in range(5):
                if bing_go[i][j] == 0:
                    sero += 1
            if sero == 5:
                bing += 1


        if bing < 3:
            bing = 0

        else:
            print(cnt)
            break
    if bing >= 3:
        break

'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
6 7 8 9 10
3 13 18 23 5
17 21 1 2 4
11 12 14 15 16
19 20 22 24 25

ans 12
'''
