import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(str, input()))

    mx = 0
    count = 0
    for i in range(1, N):
        if lst[i] == lst[i-1] == '1':
            count += 1
            if i == N -1:
                mx = max(count+1, mx)
                count = 0
        else:
            mx = max(count + 1, mx)
            count = 0
    print(f'#{tc}', mx)