import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    data = [list(map(int, input().rstrip())) for _ in range(N)]

    mid_idx = N//2
    result = 0
    idx = 0
    for i in range(N):
        result += sum(data[i][mid_idx-idx:mid_idx+idx+1])
        if i >= mid_idx:
            idx -= 1
        else:
            idx += 1
    print(f'#{tc}', result)
