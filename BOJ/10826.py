# 피보나치 수열
import sys

input = sys.stdin.readline

n = int(input())

# 1번과 2번 더하면 3번, 2번과 3번 더하면 4번.. 이러한 방법이므로 
# A는 B의 값을 받고, B는 A의 값을 더해서 받는다.
# 최종 결과값은 A
A = 0
B = 1

for i in range(n):
    A, B = B, B+A

print(A)

