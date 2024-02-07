import sys

input = sys.stdin.readline

def bitmatch(cow):
    nn = data[cow][0]
    for i in range(1, nn+1):
        room = data[cow][i]
        if not visited[room]:
            visited[room] = True
            if selected[room] == -1 or bitmatch(selected[room]):
                selected[room] = cow
                return True
    return False


# n 소의 수, m 축사의 수
n, m = map(int, input().split())

# 소 : 0번부터 시작, 축사는 1번부터 시작
# data안의 list의 0번째는 count
data = [list(map(int, input().split())) for _ in range(n)]

# 최종 selected
selected = [-1] * (m+1)

for i in range(n):
    visited = [False] * (m+1)
    bitmatch(i)
# print(selected)
print(len(set(selected))-1)
