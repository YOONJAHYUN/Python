import sys
input = sys.stdin.readline
'''
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''


def check_wheel(depth, num, dir):

    if depth == K:
        return

    # 맞닿아있는지 확인
    link = [False] * 3
    for i in range(3):
        # 같은 극이 아니다. -> 회전해야함
        if wheel[i][2] != wheel[i + 1][6]:
            link[i] = True

    # 지금 회전방향에서 다르게 가야됨..
    new_dir = dir
    # 바퀴번호를 확인하고 같이 회전할 아이를 구한다.
    while True:

        before = num -1
        next = num
        new_dir = -1 * dir
        # 왼쪽과 맞닿아있으면
        if 0 <= before < 4 and link[before]:
            tmp_left = []
            # 왼쪽 회전 시계반대 방향
            if new_dir == -1:
                tmp_left = wheel[before][1:8]+wheel[before][0]
            # 시계 방향
            else:
                tmp_left = wheel[before][7]+wheel[before][0:7]


        # 오른쪽과 맞닿아있으면
        if 0 <= next < 4 and link[next]:
            tmp_left = []
            # 왼쪽 회전 시계반대 방향
            if new_dir == -1:
                tmp_left = wheel[before][1:8] + wheel[before][0]
            # 시계 방향
            else:
                tmp_left = wheel[before][7] + wheel[before][0:7]




wheel = [list(input().rstrip()) for _ in range(4)]

# 회전횟수 K
K = int(input())

for _ in range(K):
    # dir 1시계방향 -1반시계방향
    number, dir = map(int, input().split())

    wheel_num = number - 1

    check_wheel(0, wheel_num, dir)


'''
톱니바퀴의 극이 맞닿아 있는지 확인한다.
'''


