import sys

input = sys.stdin.readline

def bitmatch(now):

    nn = data[now][0]
    for i in range(1, nn+1):
        work = data[now][i]

        if not visited[work] and selected[work] != now:
            visited[work] = True

            if selected[work] == -1 or bitmatch(selected[work]):
                selected[work] = now
                if selected.count(now) >= 2:
                    return True


    return False

# n 직원의 수 m 일의 개수
n, m = map(int, input().split())

# 직원이 할 수 있는 일 -> 일 최대 2개
data = [list(map(int, input().split())) for _ in range(n)]

# 일 -> 직원선택
selected = [-1] * (m+1)


for i in range(n):
    visited = [False] * (m+1)
    bitmatch(i)

# print(selected)
print(len(selected) - selected.count(-1))