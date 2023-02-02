import sys
input = sys.stdin.readline

scores = {}


for idx, score in enumerate(range(8)):
    scores[idx] = int(input())

score_tuple = sorted(scores.items(), key=lambda x:-x[1])

sum = 0
idx = []
for i in range(5):
    sum += score_tuple[i][1]
    idx.append(score_tuple[i][0]+1)
idx.sort()
print(sum)
print(*idx)
