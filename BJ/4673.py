number = range(1, 10001)
a = []
for i in range(1, 10001):
    num = i
    for j in range(len(str(i))):
        num += int(str(i)[j])
    a.append(num)

self_number = list(set(number).difference(a))
self_number.sort()
for num in self_number:
    print(num)

