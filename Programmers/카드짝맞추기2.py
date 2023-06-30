def solution(board, r, c):
    answer = int(1e9)
    '''
    방향키와 엔터키를 누르는 동작 각각 1
    컨트롤 키와 방향키 1

    키 조작 횟수의 최솟값을 return
    -> 완전 탐색 + 백트래킹
    -> 제일 먼저 짝맞추는걸 목표로 한다.
    -> 커서에 닿은 거 부터 찾고, 상하좌우로 돌리기..?

    카드 뒤집기는 어짜피 무조건 정해진 숫자.
    카드 뒤집는 순서. 즉 카드 좌표들간의 이동거리만 최소로 구하면 되는 문제다.

    r c에서 시작하고
    1의 좌표. 2의 좌표 .. 이런식으로 가는 방법을 하나씩 넣어봐
    '''

    # 짝끼리 리스트로 담는다.
    check_list = [[] for _ in range(7)]
    check = [[True] for _ in range(7)]

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num:
                check_list[num].append((i, j))
                check[num] = False

    pair = check.count(False)

    # 카드 뒤집기
    def cards(y, x, now1, now2, cnt, count):
        nonlocal answer
        nonlocal check_list

        if cnt >= answer:
            return

        if count == pair:
            answer = min(answer, cnt)

        # 시작점에서 now1까지의 거리 구하기
        ny1, nx1 = now1
        ny2, nx2 = now2

        if ny1 == y and nx1 == x:

            for num in range(1, 7):
                if not check[num]:
                    check[num] = True
                    one, two = check_lsit[num]
                    cards(ny2, nx2, one, two, cnt, count + 1)
                    check[num] = False

        elif ny1 == y or nx1 == x:

            for num in range(1, 7):
                if not check[num]:
                    check[num] = True
                    one, two = check_lsit[num]
                    cards(ny2, nx2, one, two, cnt + 1, count + 1)
                    check[num] = False


        else:
            for num in range(1, 7):
                if not check[num]:
                    check[num] = True
                    one, two = check_lsit[num]
                    cards(ny2, nx2, one, two, cnt + 2, count + 1)
                    check[num] = False

    # 카드 최소한의 경로를 구한다.
    for num in range(1, 7):
        if not check[num]:
            check[num] = True
            one, two = check_list[num]
            cards(r, c, one, two, 0, 0)
            check[num] = False

    return answer


print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))

