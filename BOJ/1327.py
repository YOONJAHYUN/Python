import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())

data = list(input().split())

ans = -1
q = deque()
q.append((data, 0))

sort_nums = sorted(data)

visited = set("".join(data))

 while q:
    now, cnt = q.popleft()
    if now == sort_nums:
        ans = cnt
        break
    for i in range(n-k+1):
        # next_middle = now[i:i+k]
        # next_middle.reverse()
        next_data = now[:i] + now[i:i+k][::-1] + now[i+k:]
        numbs = ''.join(next_data)
        if numbs not in visited:
            q.append((next_data, cnt+1))
            visited.add(numbs)


print(ans)