from collections import deque

def solution(land):
    answer = 0
    
    
    def BFS(i, j, idx):
        nonlocal check
        q = deque()
        q.append((i, j))
        visited[i][j] = idx
        count = 1
        while q:
            y, x = q.popleft()
            
            for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ny, nx = y+dy, x+dx
                
                if 0 <= ny < n and 0 <= nx < m and land[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = idx
                    # check[nx] = True
                    q.append((ny, nx))
                    count += 1
                    
        check.append(count)
        
    
    # n 세로 m 가로
    n = len(land)
    m = len(land[0])
    visited = [[0]*m for _ in range(n)]
    index = 1
    check = [0]
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                BFS(i, j, index)
                index += 1

    
    for w in range(m):
        ans = 0
        sset = set()
        for h in range(n):
            sset.add(visited[h][w])
        # print(sset)
        for i in sset:
            ans += check[i]
        answer = max(ans, answer)
    return answer