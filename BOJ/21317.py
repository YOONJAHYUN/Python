import sys

input = sys.stdin.readline

n = int(input())

data = [tuple(map(int, input().split())) for _ in range(n-1)]

# 매우 큰 점프 에너지
k = int(input())
answer = 5000 * n + 1

def check(depth, very, now):
    global answer

    if depth == n-1:
        answer = min(answer, now)
        return

    small, big = data[depth]

    check(depth+1, very, now+small)

    if depth + 2 < n:
        check(depth+2, very, now+big)

    if depth + 3 < n and very:
        check(depth+3, False, now + k)

check(0,True, 0)
print(answer)