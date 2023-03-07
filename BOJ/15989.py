import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())




    dp = [0, 1, 2, 3, 4, 5, 7, 8]
    if n > 6:
        for i in range(8, n+1):
            if i % 3 == 2:
                dp.append(dp[-1]+1)
            elif i%3 == 0:
                dp.append(dp[-1]+2)
            else:
                dp.append(dp[-1]+3)



    print(dp[n])
