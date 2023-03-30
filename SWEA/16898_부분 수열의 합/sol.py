import sys

sys.stdin = open('input.txt')

def my_sum(start, end, target, ans):
    global cnt

    if start == end:
        if ans == target:
            cnt += 1
        return

    if ans == target:
        cnt += 1
        return

    my_sum(start+1, end, target, ans+data[start])
    my_sum(start+1, end, target, ans)



T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    data = list(map(int, input().split()))

    cnt = 0

    my_sum(0, N, K, 0)

    print(f'#{tc}', cnt)