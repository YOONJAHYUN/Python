import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())
    answer = 0
    for i in range(a+1):
        for j in range(b+1):
            if i+j <= b:
                if c - j < a - i:
                    k = c - j
                else:
                    k = a - i
                answer = max(i*ab + j*bc + k*ca, answer)
    print(answer)