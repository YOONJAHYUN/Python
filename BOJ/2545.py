# 빈리스트를 만들고 line = input().split() 리스트안에 감싸서,, 리스트괄호열고 인풋점스프릿으로 할건데, 
# line = map(int, input().split())
import sys

input = sys.stdin.readline


T = int(input().rstrip())
# blank = input()


for i in range(T): # 테스트 케이스만큼 돌려야 함 그래서 range로 하는거
    blank = input()

    A, B, C, D = map(int, input().rstrip().split())

    # if i != T - 1:
    #     blank = input()

    # D번 이 과정을 반복해야한다.
    for j in range(D):
        # max 값을 하나씩 줄여야한다.
        
        if max(A, B, C) == A:
            A -= 1

        elif max(A, B, C) == B:
            B -= 1
        
        elif max(A, B, C) == C:
            C -= 1
    
    print(A * B * C)

