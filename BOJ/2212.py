import sys
# input = sys.stdin.readline
from itertools import combinations

sys.stdin = open('input.txt')
N = int(input())
K = int(input())

data = list(map(int, input().split()))
data.sort()
# print(data)

if K>=N:
    print(0)
else:

    if K > 2:
        ans = 1000001
        res = []

        for combi in combinations([i for i in range(N-1)], K-1):
            # print(combi)

            tmp = 0
            for j in range(K-1):
                if j == 0:
                    tmp += data[combi[j]] - data[0]

                elif j == K-2:
                    tmp += data[-1] - data[combi[j]+1]
                    tmp += data[combi[j]] - data[combi[j-1]+1]

                else:
                    tmp += data[combi[j]] - data[combi[j-1]+1]
            ans = min(tmp, ans)
            if ans == tmp:
                res = combi

        print(ans)
    else:
        ans = 10000001

        for i in range(N-1):

            tmp = 0
            tmp += data[i] - data[0]
            tmp += data[-1] - data[i+1]
            ans = min(tmp, ans)
        print(ans)
