import sys

input = sys.stdin.readline

n = int(input())

data = [input().rstrip() for _ in range(n)]

data.sort(key=lambda x: -len(x))
ans = []

for word in data:
    for i in range(len(ans)):
        if ans[i].find(word) == 0:
            break
    else:
        ans.append(word)
print(len(ans))

