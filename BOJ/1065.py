import sys

input = sys.stdin.readline

# 한수 123 345
# 한자리수 = 모두 한수
# 두자리수 = 모두 함수
# 세자리수
N = int(input().rstrip())

count = 0
if N < 100:
    print(N)
else:
    count = 99
    for i in range(100, N+1): #100
        j = str(i)
        # print(i)
        
        if int(j[0])- int(j[1]) == int(j[1]) - int(j[2]):
            count += 1

    print(count)
