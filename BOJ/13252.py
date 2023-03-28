import sys
input = sys.stdin.readline

# 모두 같은 색일 확률
def rock(m,k):

    result = 0
    color_sum = sum(N_data)
    for color in N_data:
        ans = 1
        if color >= k:
            for i in range(m):
                ans = ans * ((color-i)/color_sum)

    result += ans
    return result
# M 조약돌 종류 / N 조약돌 개수 / K 랜덤하게 뽑을 조약돌
M = int(input())
N_data = list(map(int, input().split()))
K = int(input())


print(rock(M, K))

