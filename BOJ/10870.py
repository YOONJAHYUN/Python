import sys

input = sys.stdin.readline

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n-2) + fibo(n-1)

n = int(input())
print(fibo(n))


