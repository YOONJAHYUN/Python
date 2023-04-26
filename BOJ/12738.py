from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1]
x = [A[0]]
for i in range(1, n):
    # 지금 내 숫자가 x에 마지막에 담긴 숫자보다 크다면 담아야지
    if A[i] > x[-1]:
        x.append(A[i])
        # dp도 추가
        dp.append(dp[-1]+1)
    # 만약 그렇지 않다면?
    # 다시 넣어줘.. 위치 살펴서
    else:
        # 그 인덱스를 구해
        idx = bisect_left(x, A[i])
        x[idx] = A[i]
print(dp[-1])
