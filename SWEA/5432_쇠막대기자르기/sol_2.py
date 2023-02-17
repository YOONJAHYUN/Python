import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = list(input().rstrip())

    cnt = 0
    result = 0
    for i in range(len(data)):
        if data[i] == '(':
            cnt += 1
        else:
            if data[i-1] == '(':
                cnt -= 1
                result += cnt

            else:
                result += 1
                cnt -= 1
    print(f'#{tc}', result)
