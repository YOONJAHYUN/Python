from heapq import heappush, heappop

def dijkstra(first, start, graph, n):
    INF = int(1e9)
    visited = [INF]*(n+1)
    
    q = []
    heappush(q, (first,start))
    visited[start] = 0
    
    while q:
        cost, now = heappop(q)
        
        if visited[now] < cost:
            continue
        
        for new_cost, next in graph[now]:
            res = new_cost + cost
            
            if res < visited[next]:
                visited[next] = res
                heappush(q, (res, next))
    return visited
                


def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    '''
    다익스트라를 활용해서 최적루트로 visited를 만든다.
    이후 각자 최저로 갈 수 있는 루트를 먼저 기준값으로 잡고,
    합승했을때 최저를 구한다.
    '''
    for start, end, cost in fares:
        graph[start].append((cost, end))
        graph[end].append((cost, start))
        
    result = [[int(1e9)]*(n+1)]
    
    for i in range(1, n+1):
        result.append(dijkstra(0, i, graph, n))
    
        
    for i in range(1, n+1):
        answer = min(result[s][i] + result[i][a] + result[i][b], answer)
        
        
    return answer