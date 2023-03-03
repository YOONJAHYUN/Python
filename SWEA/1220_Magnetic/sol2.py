import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # n 정사각형 테이블의 한 변의 길이
    n = int(input())
    data = [list(input().split()) for _ in range(n)]

    ans = 0
    for st in zip(*data):
        ans += ''.join(st).replace('0', '').count('12')
    print(f'#{tc}', ans)

