import sys

input = sys.stdin.readline

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면 스위치의 상태를 바꿈
# 여학생은 좌우대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 모두 상태를 바꿈 (항상 홀수)

# N 스위치의 개수
N = int(input())

# 스위치의 상태 on 1 off 2
data = list(map(int, input().split()))

# 학생수
students = int(input())

# 남학생 1 여학생 2
for _ in range(students):
    s, switch = map(int, input().split())

    # 남학생이라면
    if s == 1:
        for i in range(switch-1, N, switch):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0

    # 여학생이라면
    else:
        for j in range(0, N//2):

            if 0 <= switch-1-j < N and 0 <= switch-1+j < N and data[switch-1-j] == data[switch-1+j]:

                if data[switch-j-1] == 1:
                    data[switch-j-1] = 0
                    data[switch+j-1] = 0
                else:

                    data[switch-j-1] = 1

                    data[switch+j-1] = 1
            else:
                break

for i in range(N):

    if i != 0 and(i % 20) == 0:
        print()
    print(data[i], end=' ')

'''
25
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1
1 1

'''
