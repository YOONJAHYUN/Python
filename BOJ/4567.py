def search(arr):
    global count
    for i in range(100):
        for j in range(99):
            if arr[i][j] == 0 and arr[i][j + 1] == 1:
                count += 1
                arr[i][j + 1] = 2
            if arr[i][j] == 1 and arr[i][j + 1] == 0:
                count += 1
                arr[i][j] = 2
            if arr[i][99] == 1:
                count += 1
                arr[i][99] = 2
            if arr[i][0] == 1:
                count += 1
                arr[i][0] = 2
N = int(input())
paper = [[0]*100 for _ in range(100)]
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

papers = list(map(list, zip(*paper)))

search(paper)
for i in papers:
    print(i)
search(papers)

print(count)