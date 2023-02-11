import sys

input = sys.stdin.readline


N = int(input().rstrip())

age_name = []
for i in range(N):
    age_name.append(list(input().split()))


age_name.sort(key=lambda x:int(x[0]))


for i in range(N):
    print(int(age_name[i][0]), age_name[i][1])
