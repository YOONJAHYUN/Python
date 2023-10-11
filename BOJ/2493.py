import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
ans = [0]

for i in range(1,n):
    top = data[i]

    for j in range(i-1, -1, -1):
        if data[j] > top:
            ans.append(j+1)
            break

    else:
        ans.append(0)

print(*ans)
