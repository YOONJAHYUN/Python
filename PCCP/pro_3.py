def solution(N, bridge):
    answer = 0

    def get_high_score(length, height, score):
        nonlocal answer

        if length == N and height == 0:
            answer = max(answer, score)
            return

        if length == N and height != 0:
            return

        if (length > N):
            return

        for a, b, c in bridge:
            get_high_score(length+a, height+b, score+c)

    get_high_score(0, 0, 0)

    return answer

print(solution(10, [[3, 1, 6], [2, 1, 5], [5, -2, 10], [1, 0, 0]]))