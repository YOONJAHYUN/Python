import sys

input = sys.stdin.readline

L = int(input())
N = int(input())

cake = [0] * (L+1)
my_mx = 0
mx_idx = 0
for person in range(1, N+1):
    P, K = map(int, input().split())
    if my_mx < K-P:
        my_mx = K-P
        mx_idx = person

    for i in range(P, K+1):
        if not cake[i]:
            cake[i] = person
real_mx = 0
real_idx = 0
for i in range(1,N+1):
    if real_mx < cake.count(i):
        real_mx = cake.count(i)
        real_idx = i

print(mx_idx)
print(real_idx)