import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
# n == 0 따로 해줘야됨 ㅡ,ㅡ
if n == 0:
    print(0)
else:
    data = []
    for _ in range(n):
        p, d = map(int, input().split())
        data.append((-d, -p))
    data.sort()
    # 제일 나중
    now = data[0][0]
    ans = 0
    while True:

        q = []
        for i in range(len(data)):
            day, pay = data[i]
            if day <= now:
                heappush(q, (pay, day))
            else:
                break

        if q:
            pay, day = heappop(q)
            ans += pay

            idx = data.index((day, pay))
            data.pop(idx)

        now += 1

        if now == 0:
            break

    print(-ans)

