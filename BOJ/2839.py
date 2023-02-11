import sys

input = sys.stdin.readline

N = int(input().rstrip())


if N == 3:
    print(1)
elif N == 1:
    print(-1)
elif N == 2:
    print(-1)
elif N == 4:
    print(-1)
elif N == 5:
    print(1)
elif N == 7:
    print(-1)
elif N == 6:
    print(2)
elif N == 9:
    print(3)
elif N == 12:
    print(4)
elif N % 5 == 0:
    print(N // 5)
elif N % 5 == 1:
    print((N // 5) + 1)
elif N % 5 == 2:
    print((N // 5) + 2)
elif N % 5 == 3:
    print((N // 5) + 1)
elif N % 5 == 4:
    print((N // 5) + 2)