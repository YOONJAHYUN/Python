import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# N 나무의 수 M 나무의길이 수
N, M = map(int, input().split())

# 나무 높이 (M보다 크거나 같다)
H = list(map(int, input().split()))
# 이진탐색을 어케해라는거고
flag = False
# 이진으로 나무의 높이를 지정한다.
def binary(target, start, end):
    global flag

    if start == end:
        return

    mid = (start+end) // 2
    cnt = 0

    for i in range(N):
        if H[i] - mid > 0:
            cnt += H[i] - mid

    # taget값이 나오지 않을 수도있다.
    # target값보다 커도됨
    # 대신 한번 더 들어갓을때 작은 경우만 가능
    if cnt == target:
        print(mid)
        return

    # if cnt >= target:
        # 한번 더 돌렸는데 값이 크다면 mid반환, 작다면 그 친구의 mid 반환
        # if not flag:
        #     flag = True
        #     binary(target, start, end*2)
        #
        #     flag = False
        #
        # else:
        # print(mid)
        # return
    else:
        if cnt < target:
            binary(target, start, mid-1)
        else:
            binary(target, mid+1, end)


# 최대나무높이를 지정함
binary(M, 0, 1000000000)

