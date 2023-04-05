import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [0]+list(map(int, input().split()))
# 시간초과
# for _ in range(M):
#     i, j = map(int, input().split())
#     print(sum(numbers[i-1:j]))

for i in range(1,N+1):
    numbers[i] += numbers[i-1]

print(numbers)


for _ in range(M):
    i, j = map(int, input().split())

    print(numbers[j]-numbers[i-1])
