import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(3)]
# print(data)
ans = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
visited = []
answer = int(1e9)

q = deque()
q.append((data, 0))

while q:
    # print("아아아아", q)
    # print(visited)

    new_data, count = q.popleft()
    # print("new", new_data)
    if new_data == ans:
        answer = count
        # print("여기 정답인데")
        break

    # if new_data in visited:
    #     continue

    for i in range(3):
        for j in range(3):
            if new_data[i][j] == 0:

                for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < 3 and 0 <= nx < 3:

                        new_data[ny][nx], new_data[i][j] = new_data[i][j], new_data[ny][nx]

                        if new_data not in visited:
                            visited.append(deepcopy(new_data))
                            q.append((deepcopy(new_data), count+1))
                        new_data[ny][nx], new_data[i][j] = new_data[i][j], new_data[ny][nx]







if answer == int(1e9):
    answer = -1

# print("정답", answer)
print(answer)