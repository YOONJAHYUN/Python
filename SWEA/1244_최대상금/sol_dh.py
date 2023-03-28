def solve(depth=0):
    global result
    if depth == count:
        result = max(result, int("".join(map(str, board))))
        return

    if answer == board:
        if (count - depth) % 2:
            check = [0 for _ in range(10)]
            for i in board:
                check[i] += 1
                if check[i] >= 2:
                    result = max(result, int("".join(map(str, board))))
                    return

            board[-1], board[-2] = board[-2], board[-1]
            result = max(result, int("".join(map(str, board))))
            board[-1], board[-2] = board[-2], board[-1]

        else:
            result = max(result, int("".join(map(str, board))))

        return

    for i in range(n):
        if board[i] == answer[i]:
            continue

        for j in range(i, n):
            if answer[i] == board[j]:
                board[i], board[j] = board[j], board[i]
                solve(depth + 1)
                board[i], board[j] = board[j], board[i]


T = int(input())

for test_case in range(1, T + 1):
    board, count = input().split()
    count = int(count)
    board = list(map(int, board))
    n = len(board)

    answer = sorted(board, reverse=True)

    result = 0

    solve()

    print(f"#{test_case} {result}")