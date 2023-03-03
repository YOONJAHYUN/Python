import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
people = list(range(0, N))
S = [list(map(int, input().split()))for _ in range(N)]

combi = list(combinations(people, N//2))

combi_len = len(combi)

# print(combi)
result = 100 * combi_len

# 전체 combi를 순회한다.
for i in range(combi_len//2):
    # print(combi[i])
    # print(combi[combi_len-1-i])
    # print()
    team1 = 0
    team2 = 0
    for j in range(N//2):
        for k in range(N//2):
            a = combi[i][j]
            b = combi[i][k]
            team1 += S[a][b] + S[b][a]
            # print('ab', a, b)
            # print(S[a][b], S[b][a])
            c = combi[combi_len-1-i][j]
            d = combi[combi_len-1-i][k]
            team2 += S[c][d] + S[d][c]
    #         print('cd', c, d)
    #         print(S[c][d], S[d][c])
    # print(j, '#########', team1, team2)
    result = min(abs(team1-team2)//2, result)

print(result)

'''
백준 풀이에서 훔쳐옴
from itertools import*
N,*A=open(0)
S=sum
A=[[*map(int,i.split())]for i in A]
s=S(p:=[S(i)+S(j)for i,j in zip(A,zip(*A))])//2
print(min(abs(s-S(i))for i in combinations(p,int(N)//2)))
'''
