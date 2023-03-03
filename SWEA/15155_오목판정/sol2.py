import sys

sys.stdin = open('input.txt')

def omok(arr):
    # 배열을 순회
    for i in range(N):
        for j in range(N):
            # 델타 탐색시작
            for di,dj in ((-1,1),(0,1),(1,1),(1,0)):    # 우상향, 우향, 우하향, 하향
                # 한방향으로 5개를 탐색하는 것
                for mul in range(5):
                    ni, nj = i + di*mul, j + dj*mul
                    # 하나라도 오목이 없으면 break
                    if arr[ni][nj] !='o':
                        break
                # 한방향이라도 오목이면 yes
                else:
                     return 'YES'
    # for문을 다 순회했지만 오목이 없다면 NO
    return 'NO'

# 함수로 써보아요.
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]

    print(f'#{tc}', omok(arr))