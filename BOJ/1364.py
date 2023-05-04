import sys

input = sys.stdin.readline

n, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

lst = []
for i in range(n-1):
    lst.append(data[i+1]-data[i])
lst.sort()

print(sum(lst[0:n-k]))
