import sys
input = sys.stdin.readline

# k 참가한 사람 수
k = int(input())
# n 가로 줄의 수
n = int(input())
# 사다리 결과
res = list(input().rstrip())

start = sorted(res)
# print(result)
# 사다리
ladder = [list(input().rstrip()) for _ in range(n)]
ladder_up = []
ladder_down = []

q_idx = 0
for i in range(n):
    if ladder[i][0] == '?':
        ladder_up = ladder[0:i]
        ladder_down = ladder[i+1:]
        q_idx = i
        break

# 위 아래 사다리를 가운데까지 끌고오기
for lad in ladder_up:
    for i in range(k-1):
        if lad[i] == '-':
            start[i], start[i+1] = start[i+1], start[i]
for lad in ladder_down[::-1]:
    for i in range(k-1):
        if lad[i] == '-':
            res[i], res[i+1] = res[i+1], res[i]

# 사다리 만들기
result = []
for i in range(k-1):
    if start[i] == res[i]:
        result.append('*')
    else:
        if start[i] == res[i+1]:
            result.append('-')
        elif i != 0 and start[i] == res[i-1]:
            result.append('*')
        else:
            result = ['x' for _ in range(k-1)]
            break

print(''.join(result))


