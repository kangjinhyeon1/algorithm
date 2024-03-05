n, m = map(int, input().split())

result = {}
res = []
for i in range(1, n+1):
    for j in range(1, m+1):
        res.append(i + j)

for key in res:
    result[key] = result.get(key, 0) + 1

maxium = sorted(result.items(), key=lambda x: -x[1])

cnt = maxium[0][1]
for i in maxium:
    if i[1] == cnt:
        print(i[0])
    else:
        break
