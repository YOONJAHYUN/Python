import sys

sys.stdin = open('input.txt')
# 회전을 하지 않고 문제를 풀어보아요.
T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    # 행렬 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]