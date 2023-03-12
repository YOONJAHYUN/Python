import sys
from itertools import combinations
# 문제 조건 잘 읽기 -> 최소 한 개의 모음 + 최소 두개 자음
# 모음과 자음으로 나누고 순열로 합해보자.?
input = sys.stdin.readline

L, C = map(int, input().split())

data = list(input().split())
data.sort()
combi = list(combinations(data, L))

print(combi)

for line in combi:
    cnt1 = 0
    cnt2 = 0
    for char in line:
        if char in 'aeiou':
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >=2:
        print(''.join(line))

