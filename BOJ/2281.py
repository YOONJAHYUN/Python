import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]
print(data)

'''
칸이 넉넉할 경우, 선택할 수 있는 경우의 수 2게

1. 다음 칸에 넣기
2. 다음 줄에 넣기

-> 어떠한 선택을 했다고 가정했을 때, 이 선택이 옳은 지는,
칸이 넉넉하지 못해 무조건 다음 줄로 가는 경우에 평가가 된다.

-> 그럼 현재에 내가 선택할 수 있는 것을 모두 넣는다.

남은 칸이 넉넉하지 못한 경우는 무조건 다음줄로 가야됨
'''
dp = [[] for _ in range(n)]
dp[0].append(data[0])

for i in range(1, n):
    word_len = data[i]

    for j in dp[i-1]:
        if 0 <= j + word_len <= m-1:
            dp[i].append(j + word_len + 1)
            dp[i].append(j)
            dp[i].append(word_len)
        else:
            dp[i].append(word_len)

print(dp)