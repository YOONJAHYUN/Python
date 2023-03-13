import sys
from itertools import combinations


input = sys.stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):

    combi = list(combinations(data, i))

    for numbers in combi:
        if sum(numbers) == S:
            cnt += 1

print(cnt)