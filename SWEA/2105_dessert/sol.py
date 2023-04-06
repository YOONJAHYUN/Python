import sys
sys.stdin = open('input.txt')

direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

# 대각선으로 쭉 가다가 안되면 회전하기..!!!
def dessert(y, x, ans,ans_y, ans_x):
    # ans = []
    # ans.append(data[y][x])

    y = y
    x = x

    for k in direction:
        mul = 1

        while True:
            ny = y + k[0] * mul
            nx = x + k[1] * mul


            if (not (0 <= ny < N and 0 <= nx < N)) or (data[ny][nx] in ans):
               # y = ny - k[0]
               # x = nx - k[1]
               break

            else:
                cafe = data[ny][nx]

                # ans.append(cafe)
                mul += 1
                dessert(ny, nx, ans+[data[y][x]], y, x)

    if ans_x == x and ans_y == y:
        print(ans)
        return




T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    # 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
    # 일단 다 구한다... 그리고 중간에 백트래킹
    dessert(0, 1, [], 0, 1)
    # print(dessert(0, 1))
    # print(dessert(0, 2))
    # print(dessert(1, 1))
    # print(dessert(1, 2))
