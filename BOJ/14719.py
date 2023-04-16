# import sys
# input = sys.stdin.readline

# H 세로길이 W가로길이
H, W = map(int, input().split())

water = list(map(int, input().split()))
result = [0] * W
result[0] = water[0]
result[-1] = water[-1]
water_max = max(water)

for now in range(1, W-1):
    right = max(water[now:])
    left = max(water[:now])
    result[now] = min(right, left)


ans = 0

for i in range(W):
    save = result[i]-water[i]
    if save > 0:
        ans += save
print(ans)


'''
4 8
3 2 1 2 1 0 3 2

3 3 3 3 3 3 3 2
'''