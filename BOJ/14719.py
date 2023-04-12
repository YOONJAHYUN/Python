import sys
input = sys.stdin.readline

# H 세로길이 W가로길이
H, W = map(int, input().split())

water = list(map(int, input().split()))
result = [[] for _ in range(W)]

for now in range(1, W-1):
    left = now - 1
    right = now + 1

    while left >= 0 and right <= W-1:
        if water[left] > water[now] and water[right] > water[now]:
            break
        # 하나만 조건 만족
        if water[left] > water[now]:
            right += 1
        elif water[right] > water[now]:
            left -= 1
        else:
            left -= 1
            right += 1

    result[now].append(min(water[left], water[right])-water[now])
print(result)
# max_h = []
# for i in range(W):
#     if water[i] == H:
#         max_h.append(i)

