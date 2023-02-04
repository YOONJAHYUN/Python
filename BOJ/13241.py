import sys

input = sys.stdin.readline

# 시간초과난다... 뭘 해야하노 ㅡㅡ
A, B = map(int, input().split())

# for i in range(max(A,B), A*B+1):
#     if i % A == 0 and i % B == 0:
#        print(i)

#유클리드 호제법을 사용한다.
# A > B일때, A =B*q + r로 표현 가능
# A와 B의 최대공약수는 B와 r의 최대공약수와 같다.
# 60과 8로 생각하면, 60 = 8*7 +4
# 그럼 60과 8의 최대공약수는 8과 4의 최대공약수인 4와 같다.
# 진짜 개신기하다........ 왜 이런걸 안배우는걸까...

mul = A*B

# 최대공약수를 먼저 구하고 거기에다가 A로 나눠준다.
while B:
    if A > B:
        A, B = B, A

    B %= A
print(mul//A)