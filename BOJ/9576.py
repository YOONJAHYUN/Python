import sys

input = sys.stdin.readline

def bitmatch(now):
    # 학생이 선택한 책번호 순회
    for num in data[now]:
        # 이 책을 방문하지 않았다면?
        if not visited[num]:
            visited[num] = True
        # 아직 아무도 안골랐거나 이미 골라져있던 수가 옮길 수 있다면
            if selected[num] == -1 or bitmatch(selected[num]):
                selected[num] = now
                return True
    return False


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # 왼쪽 정점에서 연결 가능한 오른쪽 정점 번호들
    data = []
    for _ in range(m):
        a, b = map(int, input().split())
        data.append([i for i in range(a, b+1)])

    # 책이 어떤학생을 selected했는지
    selected = [-1] * (n+1)

    # 학생들 순회
    for i in range(m):
        # 책 visited : 학생 개인의 책 중복 방지
        visited = [False] * (n+1)
        bitmatch(i)

    result = 0
    for i in range(1, n+1):
        if selected[i] >= 0:
            result += 1

    print(result)


