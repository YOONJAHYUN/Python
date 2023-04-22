def solution(n):
    answer = []

    arr = [[0] * n for _ in range(n)]

    end_num = sum([i for i in range(n + 1)])

    num = 1
    y, x = 0, 0
    d = 0
    # 하, 우, 상
    dir = [(1, 0), (0, 1), (-1, -1)]

    while True:

        arr[y][x] = num

        ny = y + dir[d % 3][0]
        nx = x + dir[d % 3][1]

        if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 0:
            num += 1
            y, x = ny, nx

        else:
            d += 1
            if num == end_num:
                break

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                answer.append(arr[i][j])

    return answer