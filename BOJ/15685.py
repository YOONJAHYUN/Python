import sys

input = sys.stdin.readline

n = int(input())

# generation = {
#     0: [(0, 0), (1, 0)],
#     1: [(0, 0), (1, 0), (1, -1)],
#     2: [(0, 0), (1, 0), (1, -1), (0, -1), (0, -2)],
#     3: [(0, 0), (1, 0), (1, -1), (0, -1), (0, -2), (-1, -2), (-1, -1), (-2, -1), (-2, -2)]
# }

generation = [[(0, 0), (1, 0)]]

for gg in range(10):

    temp = generation[gg][::]
    ex, ey = generation[gg][-1]

    new_gen = generation[gg][::-1]
    for k in range(1, len(generation[gg])):
        # new_gen[k][1]

        ngx = ex - (new_gen[k][1] - new_gen[k-1][1])
        ngy = ey + (new_gen[k][0] - new_gen[k-1][0])

        temp.append((ngx, ngy))
        ex, ey = ngx, ngy

    generation.append(temp)
for i in generation:
    print(i)



'''
방향
1: x랑 y 교체 후 y쪽에 -1 곱한걸 더하기
2: x에 -1
3: x랑 y만 교체
'''


data = [[0] * 101 for _ in range(101)]


for _ in range(n):
    x, y, d, g = map(int, input().split())

    for sx, sy in generation[g]:

        if d == 1:
            sx, sy = sy, -sx
        elif d == 2:
            sx, sy = -sx, sy
        elif d == 3:
            sx, sy = sy, sx
        else:
            sx, sy = sx, sy

        data[y+sy][x+sx] = 1


for i in data:
    print(i)
ans = 0

for i in range(101):
    for j in range(101):
       if data[i][j] == 1:
            temp = 1
            for di, dj in ((1, 0), (0, 1), (1,1)):
               ni, nj = i+di, j+dj
               if 0 <= ni < 101 and 0 <= nj < 101 and data[ni][nj] == 1:
                   temp += 1

            if temp == 4:
                ans += 1

print(ans)



