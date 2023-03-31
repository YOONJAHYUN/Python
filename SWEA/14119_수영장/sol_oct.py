import sys

sys.stdin = open('input.txt')

def cheap(n, sm):
    global ans
    if ans <= sm:
        return

    if n > 12:
        ans = min(ans, sm)
        return

    cheap(n+1, sm+day*data[n])
    # 이번달에 0일을 가면 사실 day에서 최솟값이 나온거임..굳이 안넣어도됨
    cheap(n+1, sm+mon)
    cheap(n+3, sm+mon3)
    cheap(n+12, sm+year)

T = int(input())

for tc in range(1, 1+T):

    day, mon, mon3, year = map(int, input().split())

    data = [0]+list(map(int, input().split()))
    ans = 3000*365
    cheap(1, 0)
    print(f'#{tc}', ans)

