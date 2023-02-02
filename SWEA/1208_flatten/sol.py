import sys

sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input()) # 덤프 횟수
    H = list(map(int, input().split())) # 입력되는 값을 숫자형으로 바꿔줌

##############################################################
    # 0부터 100개까지 저장해야하니까 101개 곱한다.
    cnt = [0] * 101

    # 박스 개수별로 몇 개씩 있는지 정렬
    for i in range(100):
        cnt[H[i]] += 1

    # 박스 누적합을 구한다.
    for i in range(1, 101):
        cnt[i] += cnt[i-1]

    box = [0]*100

    # 박스 정렬을 한다.
    for i in range(100):
        box[cnt[H[i]]-1] = H[i]
        cnt[H[i]] -= 1

##########################################################
    for i in range(N):
        box[99] -= 1
        box[0] += 1
        for j in range(99):
            if box[j] > box[j+1]:
                box[j+1], box[j] = box[j], box[j+1]
    D = box[-1]-box[0]

    print(f'#{tc+1}', D)





