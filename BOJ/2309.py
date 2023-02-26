import sys
input = sys.stdin.readline
import itertools

nanjaeng = []
real = []
for _ in range(9):
    nanjaeng.append(int(input()))

combi = list(itertools.combinations(nanjaeng, 7))

for com in combi:
    if sum(com) == 100:

        for i in sorted(com):
            print(i)
        break

