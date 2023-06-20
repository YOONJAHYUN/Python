import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    p, q = map(int, input().split())
    heappush(data, (p, q))

computers = [0] * (n)
count = [0] * (n)

turn = 1

# 순서, 끝나는 시간, 이용자 수
cnt = 0
while data:
    next = heappop(data)

    for i in range(n):
        # 넣을 수 있으면
        if computers[i] <= next[0]:
            # 아직 아무도 안옴
            if computers[i] == 0:
                cnt += 1
            computers[i] = next[1]
            count[i] += 1
            break

print(cnt)

for i in count:
    if i != 0:
        print(i, end=" ")
'''
6
0 15
10 25
20 30
50 70
60 80
100 120

모든 사람은 싸지방에 들어왔을 때 비어있는 자리 중에서 번호가 가장 작은 자리에 앉는 것이 규칙이다.
2
4 2
'''