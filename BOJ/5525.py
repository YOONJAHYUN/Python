import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
P = 'IO'*N + 'I'
l = len(P)
cnt = 0
for i in range(M-l+1):
    if S[i:i+l] == P:
        cnt += 1

print(cnt)