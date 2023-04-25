import sys
input = sys.stdin.readline

# 문제 n 문제난이도합 L과 R사이 가장어려운문제랑 쉬운거 X

N, L, R, X = map(int, input().split())

A = list(map(int, input().split()))
cnt = 0
for i in range(1<<N):
    temp = []
    for j in range(N):

        if i&(1<<j):
            temp.append(A[j])
    temp.sort()
    if L<= sum(temp) <= R and temp[-1]-temp[0] >= X:
       cnt += 1
print(cnt)