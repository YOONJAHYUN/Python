import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def many_money(idx, a):
    # global money
    money = 0
    while True:

        if 0 <= idx+data[idx][0] <= N:
            money += data[idx][1]
            for i in range(data[idx][0]):
                consult[idx+1] = idx + 1

        if idx >= N:
            idx = 0
            break

        idx = idx + data[idx][0]
    money_zip.append(money)
    idx += a
    many_money(idx, a+1)



N = int(input())

consult = [0] * (N+1)
# print(consult)
money = 0
data = [list(map(int, input().split())) for _ in range(N)]
money_zip = []

# idx = 0

many_money(0, 0)
print(money_zip)
