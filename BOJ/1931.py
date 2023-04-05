import sys
input = sys.stdin.readline

N = int(input())

data = [tuple(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: (x[1], x[0]))
result = 0
# print(data)

last = 0

for start, end in data:
    if start >= last:
        result += 1
        last = end

print(result)


