import sys
from heapq import heappop, heappush
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_q = []
    max_q = []
    # insert = 0
    id = 0
    index = [True] * k

    for _ in range(k):
        key, num = input().split()
        num = int(num)

        # 삽입
        if key == 'I':
            heappush(min_q, (num, id))
            heappush(max_q, (-num, id))
            id += 1
        # 삭제
        else:
            if num == -1:

                while min_q:
                    num, idx = heappop(min_q)
                    if index[idx]:
                        index[idx] = False
                        break

            elif num == 1:

                while max_q:
                    num, idx = heappop(max_q)
                    if index[idx]:
                        index[idx] = False
                        break

    ans1 = None
    ans2 = None
    # print(min_q, max_q)
    # print(index)
    while min_q:
        num, idx = heappop(min_q)
        if index[idx]:
            ans1 = num
            break
    while max_q:
        num, idx = heappop(max_q)
        if index[idx]:
            ans2 = -num
            break

    if ans1 != None and ans2 != None:
        print(ans2, ans1)
    else:
        print("EMPTY")


