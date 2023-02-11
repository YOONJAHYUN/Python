# 최대공약수와 최소공배수
import sys

input = sys.stdin.readline

A, B = map(int, input().split())

# 유클리드 호제법 활용
# A와 B의 최대공약수는 A = B * q + r일 때, B와 r의 최대공약수와 같다.
# 최소공배수는 A * B / 최대공약수

mul = A * B

while B:
    if A > B:
        A, B = B, A

    B %= A

print(A)
print(mul//A)