import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    number = int(input())
    # 0을 12개 만드는 이유 : 우리는 0부터 9까지 쓰는데(총 10개)
    # i+2까지 비교해야하기 때문에 12개로 만든다!!

    c = [0] * 12

    # 숫자를 하나씩 뜯어봅시다
    for i in range(6):
        c[number % 10] += 1
        number //= 10

    j = 0
    tri = 0
    run = 0

    # j+2 = 12에 멈춰야된다.
    while j <= 10:
        if c[j] >= 3:
            c[j] -= 3
            tri += 1
            continue

        if c[j] >= 1 and c[j+1] >= 1 and c[j+2] >= 1:
            c[j] -= 1
            c[j+1] -= 1
            c[j+2] -= 1
            run += 1
            continue
        j += 1

    if run + tri == 2:
        print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)




