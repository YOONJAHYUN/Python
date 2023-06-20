import sys

input = sys.stdin.readline
'''
3
10 7 4
9
9 9 8 7 6 6 5 5 2
'''
n = int(input())
nw = list(map(int, input().split()))
m = int(input())
mw = list(map(int, input().split()))

nw.sort(reverse=True)
mw.sort(reverse=True)

cnt = 0
# print(nw)
# print(mw)
if mw[0] > nw[0]:
    print(-1)
else:

    while mw:
        idx = 0
        for i in range(n):

            if not mw:
                break

            while True:
                if len(mw) > idx:

                    if nw[i] >= mw[idx]:
                        mw.pop(idx)
                        break

                    else:
                        idx += 1
                else:
                    break
        cnt += 1
    print(cnt)