import sys
input = sys.stdin.readline
N, L = map(int, input().split())
# 입력과 동시에 좌표 오름차순 정렬
pools= sorted(tuple(map(int, input().split())) for i in range(N))

res, s = 0, 0
for start, end in pools:
  s = max(start, s)
  diff = end - s
  count = (diff + L - 1) // L
  res += count
  s += count * L

print(res)