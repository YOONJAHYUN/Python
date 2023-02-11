# N과 M(1)
import sys
import itertools

input = sys.stdin.readline
# N = 자연수
# M = 중복 없이 M개
N, M = map(int, input().split())

numbers = list(range(1, N+1))

# print(numbers)

# 부분집합으로 구하기
# ans1 = []
# for i in range(1, 1<<N): # 1부터 2**N개의 부분집합 만들어짐
#     result = []
#     for j in range(N):
#         if i & (1<<j): # 조사했는데 만약에 있다.
#             result.append(numbers[j])

#     if len(result) == M:
#         ans1.append(result)

# print(ans1)
result = list(itertools.permutations(numbers,M))
for i in result:
    print(*i)