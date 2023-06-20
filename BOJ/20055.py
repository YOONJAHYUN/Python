import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = list(map(int, input().split()))

cnt = 1
robot = [0] * n

while True:

    # tmp1 = data[-1]
    # # 컨베이어벨트 및 로봇 회전 시키기
    # for i in range(2*n-1, -1, -1):
    #     data[i] = data[i-1]
    #     if i < n:
    #         robot[i] = robot[i-1]
    #
    # robot[-1] = 0
    # robot[0] = 0
    # data[0] = tmp1

    # 문어박사님
    data.insert(0, data.pop())
    robot.pop()
    robot.insert(0, 0)
    robot[n-1] = 0

    # 로봇 회전
    for i in range(n-2, 0, -1):
        # 지금 현재 자리에 로봇이 있다면 다음칸으로 이동
        if robot[i] == 1 and data[i+1] >= 1 and robot[i+1] == 0:
            robot[i] = 0
            robot[i+1] = 1
            data[i+1] -= 1


    # 제일 앞자리에 로봇 넣기
    if data[0] >= 1:
        data[0] -= 1
        robot[0] = 1

    if data.count(0) >= k:
        print(cnt)
        break

    cnt += 1
