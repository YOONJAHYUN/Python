import sys
from collections import Counter
input = sys.stdin.readline

def R():
    for lst in data:
        counter = Counter(lst)
        new_lst = (sorted(counter.items(), key=lambda x:(x[1], x[0])))


r, c, k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(3)]

# 맨 처음 행의 개수와 열의 개수 판단
if len(data) >= len(data[0]):
    R()
else:
    C()
