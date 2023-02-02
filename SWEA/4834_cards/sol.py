import sys

sys.stdin = open('input.txt')

def my_max(list):
    mmax = list[0]
    idx = 0
    for i in range(len(list)):
        if list[i] >= mmax:
            mmax = list[i]
            idx = i

    return idx, mmax



T = int(input())

for tc in range(T):

    N = int(input())

    # counting sorts를 활용해서 숫자 개수를 세어보자.
    number = int(input())

    c = [0] * 10

    for i in range(N):
        c[number % 10] += 1
        number //= 10

    idx, mmax = my_max(c)

    print(f'#{tc+1}', idx, mmax)


