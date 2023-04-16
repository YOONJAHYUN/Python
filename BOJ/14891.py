import sys
input = sys.stdin.readline
'''
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''


def check_wheel(num, dir):
    global wheel

    # 맞닿아있는지 확인
    link = [False] * 3
    for i in range(3):
        # 같은 극이 아니다. -> 회전해야함
        if wheel[i][2] != wheel[i + 1][6]:
            link[i] = True


    # 새로 만들 wheel
    new_wheel = [[] for _ in range(4)]

    # 나를 회전 시키자
    if dir == -1:
        new_wheel[num] = wheel[num][1:8] + [wheel[num][0]]
    # 시계 방향
    else:
        new_wheel[num] = [wheel[num][7]] + wheel[num][0:7]

    # 지금 회전방향에서 다르게 가야됨..
    new_dir1 = dir
    new_dir2 = dir

    # 바퀴번호를 확인하고 같이 회전할 아이를 구한다.
    before = num - 1
    next = num

    # 왼쪽 조사
    while True:
        # while문 종료조건
        if before < 0:
            break

        new_dir1 = -1 * new_dir1
        # 왼쪽과 맞닿아있으면
        if 0 <= before < 3 and link[before]:
            tmp_left = []
            # 왼쪽 회전 시계반대 방향
            if new_dir1 == -1:
                tmp_left = wheel[before][1:8]+[wheel[before][0]]
            # 시계 방향
            else:
                tmp_left = [wheel[before][7]]+wheel[before][0:7]
            new_wheel[before] = tmp_left
            link[before] = False
            before -= 1

        # 맞닿아있지 않다면 break
        else:
            break

    # 오른쪽 조사
    while True:

        if next > 3:
            break

        new_dir2 = -1 * new_dir2

        # 오른쪽과 맞닿아있으면
        if 0 <= next < 3 and link[next]:
            tmp_right = []
            # 왼쪽 회전 시계반대 방향
            if new_dir2 == -1:
                tmp_right = wheel[next+1][1:8] + [wheel[next+1][0]]
            # 시계 방향
            else:
                tmp_right = [wheel[next+1][7]] + wheel[next+1][0:7]
            new_wheel[next+1] = tmp_right

            link[next] = False
            next += 1
        else:
            break

    # 회전 시킨 후

    for i in range(4):
        if new_wheel[i]:
            wheel[i] = new_wheel[i]

    # for i in wheel:
    #     print(i)


wheel = [list(input().rstrip()) for _ in range(4)]

# 회전횟수 K
K = int(input())

for _ in range(K):
    # dir 1시계방향 -1반시계방향
    number, dir = map(int, input().split())

    wheel_num = number - 1

    check_wheel(wheel_num, dir)

ans = 0
for i in range(4):
    if wheel[i][0] == '1':
        ans += (2**i)

print(ans)