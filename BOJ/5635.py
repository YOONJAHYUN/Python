import sys

input = sys.stdin.readline


n = int(input().rstrip())

students=[]

for i in range(n):
    students += [list(input().rstrip().split())]
    
    
students.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))


print(students[-1][0])
print(students[0][0])