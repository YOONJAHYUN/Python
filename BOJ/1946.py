import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    score = [[] for _ in range(N+1)]
    for _ in range(N):
        score1, score2 = map(int, input().split())
        score[score1] = score2
    # print(score)

    cnt = 1
    lucky = []
    lucky.append(score[1])
    my_min = lucky[0]
    for i in range(2, N+1):
        if score[i] < my_min:
            my_min = min(my_min, score[i])
            cnt += 1
            lucky.append(score[i])
    # print(lucky)

    print(cnt)