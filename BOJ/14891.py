import sys
input = sys.stdin.readline
'''
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
'''

wheel = [list(input().rstrip()) for _ in range(4)]

# 회전횟수 K
K = int(input())

for _ in range(K):
    # dir 1시계방향 -1반시계방향
    number, dir = map(int, input().split())

    wheel_num = number - 1

    # score(wheel_num,dir)

link = [False] * 3

# 맞닿아있는지 확인
for i in range(3):
    # 같은 극이 아니다. -> 회전해야함
    if wheel[i][2] != wheel[i+1][6]:
        link[i] = True






