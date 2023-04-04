import sys
sys.stdin = open('input.txt')
'''
#1 5
#2 8
#3 9
'''
# dp로 풀면 안됨 ;;
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # print(tc)
    # data = [[1000]*(N+1)]+ [[1000]+list(map(int, input().split())) for _ in range(N)]
    data = [list(map(int, input().split())) for _ in range(N)]
    new_data = [[0]*N for _ in range(N)]
    for i in data:
        print(i)
    print()
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                new_data[i][j] = data[i][j]

            elif i == 0:

                new_data[i][j] = max(data[i][j]-data[i][j-1],0) + 1 + new_data[i][j-1]

            elif j == 0:

                new_data[i][j] = max(data[i][j]-data[i-1][j],0) + 1 + new_data[i-1][j]

            else:
                route1 = max(data[i][j] - data[i-1][j], 0) + new_data[i-1][j]
                route2 = max(data[i][j] - data[i][j-1], 0) + new_data[i][j-1]
                # route3 = max(data[i][j] - data[i][j+1], 0) + new_data[i-1][j+1]

                new_data[i][j] = min(route1, route2) + 1

    for i in new_data:
        print(i)
    print()
    print(f'#{tc}', new_data[-1][-1])