import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')
n, h = map(int, input().split())

result = [0] * h

for i in range(n):
    high = int(input())
    # 아래부터 자라는 석순의 경우
    # 인덱스값을 1이 아닌 0으로 접근하고 있기 때문에, 0을 1이라고 생각하는 중
    # 그래서, 무조건 1번째자리는 차오르니까 0에 1을 넣어준거
    # 그리고 그 높이는 high-1이니까 high까지 여기까지 왔다고 표시해주는 걸로 -1로 표기
    if i%2:
        result[high] -= 1
        result[0] += 1
    else:
        result[h-high] += 1

# 누적합을 따로
for i in range(1, h):
    result[i] += result[i-1]

my_min = (n+1)
cnt = 0
for i in range(h):
    if my_min > result[i]:
        my_min = result[i]
        cnt = 1
    elif my_min == result[i]:
        cnt += 1
print(my_min, cnt)