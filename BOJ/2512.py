import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())

if sum(data)<= m:
    print(max(data))
else:
    start = 1
    end = 100000

    while start <= end:

        mid = (start+end) // 2

        count = 0
        for money in data:
            if money >= mid:
                count += mid
            else:
                count += money

        # count가 예산보다 클 경우 -> 상한액을 줄인다.
        if count > m:
            end = mid - 1
        else:
            start = mid + 1

    print(end)