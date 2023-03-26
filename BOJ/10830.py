import sys
import copy

input = sys.stdin.readline

N, B = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

result = [[0]*N for _ in range(N)]
temp = copy.deepcopy(data)

for _ in range(B-1):
    for i in range(N):
        for j in range(N):
            ans = 0
            for k in range(N):
                ans += temp[i][k] * data[k][j]
            result[i][j] = (ans % 1000)
    tmp = copy.deepcopy(result)
    temp = copy.deepcopy(tmp)

for lst in temp:
    for num in lst:
        print(num, end=' ')
    print()
