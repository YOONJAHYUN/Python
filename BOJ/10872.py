import sys

input = sys.stdin.readline

def factorial(n):

    if n == 0:
        return 1

    if n == 1:
        return 1


    return factorial(n-1) * n




n = int(input())

print(factorial(n))
