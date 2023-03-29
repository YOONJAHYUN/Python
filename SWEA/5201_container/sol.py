import sys

sys.stdin = open('input.txt')


t = int(input())

for tc in range(1, t+1):
    # N 컨테이너 M 트럭
    N, M = map(int, input().split())

    # 화물의 무게
    W = list(map(int, input().split()))
    W.sort(reverse=True)

    # 트럭의 적재 용량
    T = list(map(int, input().split()))
    T.sort(reverse=True)

    # print(W)
    # print(T)
    # print()
    ans = 0
    idx = 0
    for i in range(M):
        while True:
            if idx == N:
                break
            if T[i] >= W[idx]:
                ans += W[idx]
                idx += 1
                break
            else:
                idx += 1
    print(f'#{tc}', ans)

