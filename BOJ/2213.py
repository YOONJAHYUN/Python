import sys
input = sys.stdin.readline

n = int(input())
# 정점 가중치
data = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
# 간선의 리스트
while True:
    try:
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break

print(graph)

'''
1과 연결된 2는 안됨
2랑 연결된 3은 됨..
이런식으로... 

1에서 시작해서 graph에 2는 있으니 건너.. 2의 자식인 3과 6..
3을 선택.. 그리고 3과 연결된 4는 안되고,
4와 연결된 5 선택... 

6을 선택.. 2랑 7은 안됨
근데 6보다 7을 선택하는게 이득임..

dp 형식으로 풀어야할거같음
dp 를 구해놓고, dp = [0] * (n+1)
1에서 시작..?

아니면 1선택.. 그리고 2로 갓을때 1과 연결되는지 확인.. 이런식으로..
그러면 
'''

dp = [[0]*(n+1) for _ in range(2)]

dp[0][1] = 0
dp[1][1] = data[1]
for i in range(2, n+1):

    # 연결된 노드가 아니라면 선택하는 게 이득이지만, 그전에꺼에서 선택안했던게 이득 일 수 도
    if i-1 not in graph[i]:
        dp[1][i] += data[i]
        dp[1][i] += max(dp[1][i-1], dp[0][i-1])

print(dp)