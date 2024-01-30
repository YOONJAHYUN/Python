import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# 사진 틀의 개수
n = int(input())

# 전체 학생 수
m = int(input())
students = list(map(int, input().split()))

q1 = []
q2 = []


for i in range(1, m+1):
    student = students[i-1]
    flag = False

    while q1:
        cnt, idx, stu = heappop(q1)

        if stu == student:
            heappush(q2, (cnt+1, idx, stu))
            flag = True
        else:
            heappush(q2, (cnt, idx, stu))

    if not flag:
        if len(q2) == n:
            heappop(q2)
        heappush(q2, (1, i, student))

    q1 = q2
    q2 = []

q1.sort(key=lambda x: x[2])
for cnt, idx, stu in q1:
    print(stu, end=" ")