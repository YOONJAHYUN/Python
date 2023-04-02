import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, *data = input().split()

    number = ''
    for num in data[0]:
        my_num = format(int(num, 16),'b').zfill(4)
        number += my_num
    print(f'#{tc}',number)

