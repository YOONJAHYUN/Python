import sys

input = sys.stdin.readline

AN, AM = map(int, input().split())

data1 = [list(map(int, input().split())) for _ in range(AN)]

BM, BK = map(int, input().split())

data2 = [list(map(int, input().split())) for _ in range(BM)]
print(data1)

ans = 0
for i in range(AM):
    ans += data1[j][i]*data2[i][k]
# for i in result:
#     print(*i)