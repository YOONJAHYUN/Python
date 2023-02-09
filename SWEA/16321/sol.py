import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    # ans를 미리 지정하기
    ans = 'yes'

    # [1] si,sj, ei,ej 좌표 찾기
    si = sj = N
    ei = ej = 0
    for i in range(N):
        for j in range(N):
            # '#'를 찾았다 -> 좌표를 기록하자..
            #
            if arr[i][j] == '#':
                # 세로로 가장 작은 인덱싱 = si
                if si > i:
                    si = i
                # 가로로 가장 작은 인덱싱 = sj
                if sj > j:
                    sj = j
                # 세로로 가장 큰 인덱싱 = ei
                if ei < i:
                    ei = i
                # 가로로 가장 큰 인덱싱 = ej
                if ej < j:
                    ej = j

    # 길이가 다르면 정사각형 아니다
    if (ei - si) != (ej - sj):  # 정사각형 아님
        ans = 'no'
    # 길이가 같아도 연속으로 없으면 아니다.
    else:
        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                if arr[i][j] != '#':
                    ans = 'no'

    print(f'#{test_case} {ans}')