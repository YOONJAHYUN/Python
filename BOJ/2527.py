import sys

input = sys.stdin.readline

# a 직사각형 b 선분 c 점 d 공통부분이 없음
# 직사각형이 되는 조건
# 두번째 직사각형이 첫번째 직사각형 범위안에 하나라도 들어있으면 됨

for _ in range(4):

    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 직사각형
    if (x1 <= x2 <= p1 and y1 <= y2 <= q1) or(x1 <= p2 <= p1 and y1 <= q2 <= q1) or (x2 <= x1 <= p2 and y2 <= y1 <= q2) or(x2 <= p1 <= p2 and y2 <= q1 <= q2) or (x1<=x2<=p1 and x1<=p2<=p1 and y1<=y2<=q2 and y1<=q2):
        if (x1 == p2 and q1>y2>y1) or (y1 == q2 and x1<x2<p1) or (p1 == x2 and y1 < y2 < q1)or (p1 == y2 and x1<x2<p1) :
            print('b')
        elif (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2) or (q1 == x2 and y1 == q2):
            print('c')
        else:
            print('a')
    # 선분이 되는 조건
    elif (x1 == p2 and q1>y2>y1) or (y1 == q2 and x1<x2<p1) or (p1 == x2 and y1 < y2 < q1)or (p1 == y2 and x1<x2<p1) :
        print('b')


    # 점이 되는 조건
    elif (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2) or (q1 == x2 and y1 == q2):
        print('c')
    # 공통부분이 없음
    # elif p1 < x2 or q1 < y2 or y2 < q1 or p2 < x1:
    #     print('d')

    else:
        print('d')

'''
2 2 3 3 3 3 4 4   
2 2 3 3 1 1 2 2
2 2 3 3 3 1 4 2
2 2 3 3 1 3 2 4
'''

