import sys

input = sys.stdin.readline

# N 전체 날짜 수
# K 합을 구하기 위한 연속적인 날짜의 수
N, K = map(int, input().split())
data = list(map(int, input().split()))
ans = sum(data[0:K])
result = sum(data[0:K])

for i in range(N-K):
    result -= data[i]
    result += data[i+K]
    if ans < result:
        ans = result

print(ans)