import sys

input = sys.stdin.readline

# a 직사각형 b 선분 c 점 d 공통부분이 없음
# 직사각형이 되는 조건
# 두번째 직사각형이 첫번째 직사각형 범위안에 하나라도 들어있으면 됨

for _ in range(4):

    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    square1_x = set(range(x1, p1+1))
    square1_y = set(range(y1, q1+1))

    square2_x = set(range(x2, p2+1))
    square2_y = set(range(y2, q2+1))

    x = square2_x & square1_x   # x 교집합
    y = square1_y & square2_y   # y 교집합


    if not all([x, y]):
        print('d')
    else:
        if len(x) == 1 and len(y) == 1:
            print('c')
        elif len(x) == 1 or len(y) == 1:
            print('b')
        else:
            print('a')

