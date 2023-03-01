import sys

input = sys.stdin.readline

w, h = map(int, input().split())
# 상점의 개수
n = int(input())

def distance(location, dir):

    if location == 1:
        return h + dir
    elif location == 2:
        return 2 * h + 2 * w - dir
    elif location == 3:
        return h-dir
    else:
        return h + w + dir


stores = []
for i in range(n+1):
    if i != n:
        stores.append(list(map(int, input().split())))
    else:
        direction, road = map(int, input().split())

result = 0
# 거리를 측정하는 방법 2가지.
# 시계방향과 반시계방향
# 효율적으로 구하기 위해서는 그냥 출발지를 일정하게 두고, 그 차이를 구하는 방식

# print(distance(direction,road))

for a, b in stores:
    # print(distance(a,b))
    path = abs(distance(a,b)-distance(direction,road))
    result += min(path, abs(2*w+2*h - path))
    # print(path)
    # print(abs(2*w+2*h - path))
#     print()
print(result)
