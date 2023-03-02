import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    # M칸의 파리..
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    # 십자가모양으로 죽이기
    max_killing = 0
    for i in range(N):

        for j in range(N):
            killing1 = 0
            killing2 = 0
            killing1 += data[i][j]
            killing2 += data[i][j]
            for k in range(1, M):
                if 0<= i < N and 0 <= j+k < N:
                    killing1 += data[i][j+k]
                if 0 <= i < N and 0 <= j-k < N:
                    killing1 += data[i][j-k]
                if 0 <= i+k < N and 0 <= j < N:
                    killing1 += data[i+k][j]
                if 0 <= i-k < N and 0 <= j < N:
                    killing1 += data[i-k][j]

                if 0 <= i+k < N and 0 <= j+k < N:
                    killing2 += data[i + k][j+k]
                if 0 <= i-k < N and 0 <= j-k < N:
                    killing2 += data[i - k][j-k]
                if 0 <= i+k < N and 0 <= j-k < N:
                    killing2 += data[i + k][j-k]
                if 0 <= i-k < N and 0 <= j+k < N:
                    killing2 += data[i - k][j+k]

            max_killing = max(max_killing, killing1, killing2)

    print(f'#{tc}', max_killing)