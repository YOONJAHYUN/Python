import sys
input = sys.stdin.readline

# n 폭우
# l 널빤지 길이
n, l = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]

data.sort()

count = 0
# 현재까지 깔린 널빤지 마지막 위치
rest = 0

for start, end in data:

    # 마지막 위치가 현재 시작 위치보다 클 경우
    if rest > start:
        # 시작 위치를 마지막에다 둠
        start = rest

    # WHILE문을 돌려서
    while start < end:
        # 널빤지 하나 설치하면 그만큼 길이가 늘어남
        start += l
        count += 1
    # 마지막꺼는 마지막에 START 위치임
    rest = start

print(count)




