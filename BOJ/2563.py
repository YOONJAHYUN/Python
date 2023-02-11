import sys

input = sys.stdin.readline

N = int(input().rstrip())
paper = [[0 for _ in range(100)] for _ in range(100)]


for i in range(N):
    x, y = map(int, input().rstrip().split())


    for i in range(10):
        for j in range(10):
            paper[x + i][y + j] = 1
        
count = 0

# for i in range(100):
#     for j in range(100): 
#         if paper[i][j] == 1:
#             count += 1


# count 메소드를 써서 할 수 있다.
for i in paper:
    count += paper.count(1)

print(count)



