import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
result = [-1] * n

q = []

for i in range(n):

    while q and (q[-1][0] < data[i]):
        val, idx = q.pop()
        result[idx] = data[i]
    q.append((data[i],i))
print(*result)