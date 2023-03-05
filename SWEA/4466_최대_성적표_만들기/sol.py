import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    scores.sort(reverse=True)
    print(f'#{tc}', sum(scores[0:K]))