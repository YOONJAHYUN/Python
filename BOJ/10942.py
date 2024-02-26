import sys
input = sys.stdin.readline


n = int(input())
data = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# visited = dict()

def check(i, j):
    # visited[(i, j)] = 1
    visited[i][j] = True

    if i == j:
        dp[i][j] = 1
        return

    if data[i] == data[j]:
        num1, num2 = i+1, j-1

        while num1 <= num2:
            if data[num1] == data[num2]:
                num1 += 1
                num2 -= 1
            else:
                dp[i][j] = 0
                break
        else:
            dp[i][j] = 1


for _ in range(m):
    a, b = map(int, input().split())
    if not visited[a-1][b-1]:
        check(a-1, b-1)
    print(dp[a-1][b-1])

