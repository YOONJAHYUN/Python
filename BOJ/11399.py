import sys

input = sys.stdin.readline


N = int(input())

P = list(map(int, input().split()))
P.sort()

for i in range(1,N):
    P[i] = P[i-1] + P[i]

print(sum(P))