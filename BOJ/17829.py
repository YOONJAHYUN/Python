import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

def pulling(n, x, y, arr, result):

    if n == 2:
        ans = []
        for i in range(y, y + n):
            for j in range(x, x + n):
                ans.append(arr[i][j])
        ans.sort()
        # print(ans)
        # print(ans[2])
        # print()


        result[y//2][x//2] = ans[2]
        # print(result)
        # return
        # return result
    else:

        pulling(n//2, x, y, arr, result)
        pulling(n//2, x+n//2, y, arr, result)
        pulling(n//2, x, y+n//2, arr, result)
        pulling(n//2, x+n//2, y+n//2, arr, result)

    # return pulling(n//2, 0, 0, result, [[0]*(n//2) for _ in range(N//2)])
    return result

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

# print(pulling(N, 0, 0, data, [[0]*(N//2) for _ in range(N//2)]))

n = N

a = int(math.log2(N))

new_data = pulling(n, 0, 0, data, [[0] * (n // 2) for _ in range(n // 2)])

for j in range(a-1):
    n //= 2
    new_data = pulling(n, 0, 0, new_data, [[0] * (n // 2) for _ in range(n // 2)])
print(new_data[0][0])

