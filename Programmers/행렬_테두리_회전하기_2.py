def solution(rows, columns, queries):
    answer = []

    arr = []

    for i in range(1, columns * rows, columns):
        temp = [j for j in range(i, i + rows)]
        arr.append(temp)

    for query in queries:
        start_row, start_column, end_row, end_column = query
        sr, sc, er, ec = start_row - 1, start_column - 1, end_row - 1, end_column - 1

        temp = arr[sr][sc]

        min_ans = temp

        for i in range(sr + 1, er + 1):
            arr[i - 1][sc] = arr[i][sc]
            min_ans = min(min_ans, arr[i][sc])

        for i in range(sc + 1, ec + 1):
            arr[sr][i - 1] = arr[sr][i]
            min_ans = min(min_ans, arr[sr][i])

        for i in range(er - 1, sr - 1, -1):
            arr[i + 1][ec] = arr[i][ec]
            min_ans = min(min_ans, arr[i][ec])

        for i in range(ec - 1, sc - 1, -1):
            arr[sr][i + 1] = arr[sr][i]
            min_ans = min(min_ans, arr[sr][i])

        arr[sr][sc + 1] = temp

        answer.append(min_ans)

    return answer