import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []

ans = []
for i in range(n):

    num = int(input())

    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    # 최댓값맨앞 -> 즉, 중앙값이 min의 첫번째 보다 크다면 이건 더 이상 중앙값이 아님
    # 그래서 교체 해줘야됨
    if min_heap and -max_heap[0] > min_heap[0]:

        num1 = heappop(max_heap)
        num2 = heappop(min_heap)

        heappush(max_heap, -num2)
        heappush(min_heap, -num1)

    ans.append(-max_heap[0])

for num in ans:
    print(num)

