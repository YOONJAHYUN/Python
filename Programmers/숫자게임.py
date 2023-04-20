def solution(A, B):
    answer = 0

    n = len(A)
    A.sort()
    B.sort()

    i = 0
    j = 0

    while j < n:
        if B[j] > A[i]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1

    return answer