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

        # 대각선 빙고
        daegak1 =0
        daegak2 = 0
        for i in range(5):
            if bing_go[i][i] == 0:
                daegak1 += 1
            if bing_go[4-i][i] == 0:
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
        sero = 0
        for j in range(5):
            for i in range(5):
                if bing_go[i][j] == 0:
                    sero += 1
            if sero == 5:
                bing += 1

        if bing >= 3:
            print(cnt)
            break
        else:
            bing = 0
'''
14 12 5 11 13 
9 4 3 8 25 
18 15 19 24 20 
1 6 7 23 17 
22 16 10 2 21 

17 11 9 24 6 
23 1 2 15 12 
8 14 21 10 16 
3 22 18 13 25 
4 5 19 7 20
'''
