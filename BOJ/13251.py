import sys
input = sys.stdin.readline

# 모두 같은 색일 확률

# M 조약돌 종류 / N 각각 조약돌 개수 / K 랜덤하게 뽑을 조약돌
M = int(input())
N_data = list(map(int, input().split()))

# 전체 조약돌 개수
N = sum(N_data)

K = int(input())

'''
(색 남은 양) / (전체 개수)

색 남은 양에서 하나씩 빼기
'''

result = 0

for i in range(M):
    ans = 1
    idx = 0
    if N_data[i] >= K:
        while idx < K:
            ans = ans * ((N_data[i] - idx) / (N - idx))
            idx += 1

        result += ans


print(result)



