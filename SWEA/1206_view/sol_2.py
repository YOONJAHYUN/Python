import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    h = list(map(int, input().split()))

    count = 0
    for i in range(2, len(h)-1):
        if h[i] - h[i-1] > 0 and h[i] - h[i-2] > 0 and h[i] - h[i+1] > 0 and h[i] - h[i+2] > 0:
            count += min(h[i] - h[i-1], h[i] - h[i-2], h[i] - h[i+1], h[i] - h[i+2])

    print(f'#{tc}', count)