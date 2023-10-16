def solution(rows, columns, queries):
    answer = []

    arr = []

    for i in range(1, columns * rows, columns):
        temp = [j for j in range(i, i + rows)]
        arr.append(temp)

    for query in queries:
        start_row, start_column, end_row, end_column = query
        sr, sc, er, ec = start_row - 1, start_column - 1, end_row - 1, end_column - 1

        start_row = sr
        start_col = sc

        temp = arr[start_row][start_col]

        start_col += 1
        min_ans = temp

        while True:
            min_ans = min(min_ans, temp)

            if start_row == sr and start_col <= ec:

                if start_row == sr and start_col == sc:
                    arr[start_row][start_col] = temp

                    min_ans = min(min_ans, temp)
                    break

                arr[start_row][start_col], temp = temp, arr[start_row][start_col]
                if start_col == ec:
                    start_row += 1
                else:
                    start_col += 1
            elif start_col == ec and start_row <= er:
                arr[start_row][start_col], temp = temp, arr[start_row][start_col]
                if start_row == er:
                    start_col -= 1
                else:
                    start_row += 1

            elif start_row == er and start_col >= sc:
                arr[start_row][start_col], temp = temp, arr[start_row][start_col]
                if start_col == sc:
                    start_row -= 1
                else:
                    start_col -= 1

            else:
                arr[start_row][start_col], temp = temp, arr[start_row][start_col]
                if start_row == sr:
                    break
                else:
                    start_row -= 1

        for i in arr:
            print(i)
        print("##################")
        answer.append(min_ans)
    return answer


solution(, 6, [[2,2,5,4],[3, 3, 6, 6], [5, 1, 6, 3]])