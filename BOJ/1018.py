# 체스
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]

# 8*8 배열을 쭈욱 찾는다.
# 조건을 두개로 W로 시작. B로 시작.
# 배열로 찾으면서 count를 세고 젤 작은 숫자를 반환

# 첫시작이 W이면 W 32 B 32개

# 전체 행렬을 순회한다.
# 근데, 8* 8로..
c1 = []
for _ in range(4):
    c1.append(['W', 'B']*4)
    c1.append(['B', 'W']*4)

c2 = []
for _ in range(4):
    c2.append(['B', 'W']*4)
    c2.append(['W', 'B']*4)

result1 = []
for i in range(M-7):
    for j in range(N-7):
        count1 = 0
        for x in range(8):
            for y in range(8):

                if arr[j+y][i+x] != c1[y][x]:
                    count1 += 1

        result1.append(count1) 

A = min(result1)
# print(arr)


result2 = []
for i in range(M-7):
    for j in range(N-7):
        count2 = 0
        for x in range(8):
            for y in range(8):

                if arr[j+y][i+x] != c2[y][x]:
                    count2 += 1

        result2.append(count2)

B = min(result2)
print(min(A, B))


