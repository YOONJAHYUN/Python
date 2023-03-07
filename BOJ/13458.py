import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for student in A:
    if student <= B:
        cnt += 1
    elif student <= B+C:
        cnt += 2
    else:
        stu = student - (B+C)
        cnt += 2
        if stu % C:
            cnt += stu // C + 1
        else:
            cnt += stu // C

print(cnt)

'''
8
5 10 30 235 1 23 24 101
10 3
1 1 10+3+3+3+3+3+3+3
'''