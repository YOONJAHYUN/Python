import sys

sys.stdin = open("input.txt")

TC = int(input())
for T in range(1, TC + 1):
    N, K = map(int, input().split())
    mat = []  # 리스트들을 받을 행렬 생성

    result = []
    cnt = 0
    for i in range(N):
        ls = list(map(int, input().split()))
        mat.append(ls)

    # 가로로 한줄씩 가면서
    # 1의 개수를 셈 그리고 0을 만나면 result 행렬에 저장
    for i in mat:
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)
    cnt = 0

    # 아래건 세로로 했다
    # 가로랑 똑 같음
    for i in range(N):
        cnt = 0
        for j in range(N):
            if mat[j][i] == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)
    res = 0

    # 위의 작업이 끝나고 result안의 K의 개수를 셈
    for i in result:
        if i == K:
            res += 1
    print(f"#{T}", res)