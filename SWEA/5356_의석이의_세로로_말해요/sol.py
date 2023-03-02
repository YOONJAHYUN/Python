import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = []
    for _ in range(5):
        data.append(list(map(str, input().rstrip())))
    max_len = 0
    for i in data:
        max_len = max(len(i), max_len)
    # print(max_len)

    result = ''
    for i in range(max_len):
        for j in range(5):
            try:
                result += data[j][i]
            except:
                pass

    print(f'#{tc}', result)