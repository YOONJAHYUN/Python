import sys
sys.stdin = open('input.txt')
T = int(input())

# 블록의 개수가 젤 큰게 낙차가 젤 크다

for i in range(T):
    N = int(input())
    blocks = list(map(int, input().split()))

    max_block = 0

    # 블록 본인보다 작은 블록의 개수를 세고 저장한다.
    # 저장된 블록 중에서 가장 큰 값을 보여준다.

    for i in range(len(blocks)):
        count = 0
        for j in range(len(blocks) - i):
            if blocks[i] > blocks[i+j]:
                count += 1

        if max_block < count:
            max_block = count

    print(f'#{i+1} {max_block}')