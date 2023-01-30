A, B = map(int, input().split())
C = int(input())

B = B + C
# 60분은 나올 수 없으므로 60분이상인 동안 반복해준다
while B >= 60:
        B -= 60
        if A == 23:
            A = 0
        else:
            A += 1
        
print(A, B)