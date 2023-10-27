import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

tag = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7],
]


data = ""
for i in range(3):
    data += "".join(input().split())
# data = "".join()

# print(data)
x = data.find("0")

# x = data.index("0")
# print(x)
# print(data[x])
# print(data)
answer = "123456780"
q = deque()
dict ={}
dict[data] = 1
# visited = [deepcopy(data)]
q.append((x, 0, data))

# print(data)

while q:

    now, count, now_data = q.popleft()

    if answer == now_data:
        # print("정답")
        print(count)
        # print(now, count, now_data)
        exit(0)


    for num in tag[now]:
        list_data = list(now_data)
        list_data[now], list_data[num] = list_data[num], list_data[now]
        new_data = "".join(list_data)

        if dict.get(new_data):
            continue
        else:
            dict[new_data] = 1
            q.append((num, count+1, new_data))

print(-1)