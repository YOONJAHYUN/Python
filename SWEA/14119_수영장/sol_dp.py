import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):

    day, mon, mon3, year = map(int, input().split())

    data = [0]+list(map(int, input().split()))
    ans = 3000*365

    # 규칙성 찾기
    s = [0] * 13
    for i in range(1, 13):
        # 가능한 i달까지의 최소비용
        s[i] = s[i-1]+day*data[i] # 일간권
        s[i] = min(s[i], s[i-1]+mon)
        if i >= 3:
            s[i] = min(s[i], s[i-3]+mon3)

        if i >= 12:
            s[i] = min(s[i], s[i-12]+year)

    print(f'#{tc}',s[12])
