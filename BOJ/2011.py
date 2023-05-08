import sys

input = sys.stdin.readline

number = '0'+input()

dp = [0 for _ in range(len(number)-1)]


if number[1] == '0' or len(number) == 1:
    print(0)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(number)-1):
        if number[i] == '0':
            if number[i-1] == '1' or number[i-1] == '2':

                dp[i] = dp[i-2]
            else:
                print(0)
                exit(0)
        elif number[i-1] == '0':
            dp[i] = dp[i-1]
        elif int(number[i-1] + number[i]) <= 26:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]

    print(dp[-1]%1000000)