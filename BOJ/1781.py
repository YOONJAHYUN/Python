import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
tasks = [list(map(int, input().split())) for _ in range(n)]

# 데드라인에 따라 오름차순으로 정렬
tasks.sort(key=lambda x: x[0])

# 컵라면 수를 최대로 하기 위한 우선순위 큐
pq = [] # 컵라면 수를 저장하는 우선순위 큐
for deadline, cup in tasks:
    heappush(pq, cup)  # 현재 작업을 우선순위 큐에 추가
    # 현재까지 선택한 작업의 수가 데드라인을 초과한다면, 가장 컵라면 수가 적은 작업을 제거
    if len(pq) > deadline:
        heappop(pq)

# 우선순위 큐에 남아 있는 컵라면의 수의 합이 최대 컵라면 수
answer = sum(pq)

print(answer)
