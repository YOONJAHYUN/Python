import sys

input = sys.stdin.readline

data1 = input().rstrip()
data2 = input().rstrip()

n1 = len(data1)
n2 = len(data2)

ans = 0
i = 0

while i <= n1-n2:
    if data1[i:i+n2] == data2:
        ans += 1
        i += n2
    else:
        i += 1

print(ans)

